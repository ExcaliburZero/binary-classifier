#!/bin/python2
"""Runs the program."""

import EmulatorMain
import SimpleClassifier

import cli.app


@cli.app.CommandLineApp
def main(app):
    """
    Generates test data, categorizes the data into transient types, and
    prints out the results.
    """

    # Decide on the number of transients and non transient to generate
    total_objects = app.params.number
    number_transients = total_objects / 2
    number_non_transients = total_objects - number_transients

    if app.params.verbose:
        main_verbose(number_transients, number_non_transients)
    else:
        main_simple(number_transients, number_non_transients)


def main_simple(number_transients, number_non_transients):
    emulator = EmulatorMain.EmulatorMain()

    # Analyze the transients
    correct_transients = 0
    for _ in range(0, number_transients):
        transient = emulator.generateSingleObject(True)
        results = SimpleClassifier.classify_simple(transient)
        if results:
            correct_transients += 1
    print "Transients:     " + str(correct_transients) + " / " + str(number_transients)

    # Analyze the non-transients
    correct_non_transients = 0
    for _ in range(0, number_non_transients):
        non_transient = emulator.generateSingleObject(False)
        results = SimpleClassifier.classify_simple(non_transient)
        if not results:
            correct_non_transients += 1
        else:
            print non_transient

    print "Non-Transients: " + str(correct_non_transients) + " / " + str(number_non_transients)


def main_verbose(number_transients, number_non_transients):
    print "Generating test transient data..."

    # Generate the test data
    emulator = EmulatorMain.EmulatorMain()
    transient_graphs = [emulator.generateSingleObject(True) for x in range(0, number_transients)]
    non_transient_graphs = [emulator.generateSingleObject(False) for x in range(0, number_non_transients)]

    # Classify the transient and non-transients
    print "Categorizing transients..."
    transient_results = map(SimpleClassifier.classify_simple, transient_graphs)
    non_transient_results = map(SimpleClassifier.classify_simple, non_transient_graphs)

    # Transform the results into strings
    transient_strings = []
    for transient_info in zip(transient_graphs, transient_results):
        transient_strings = transient_strings + [transient_to_string(True, transient_info)]

    non_transient_strings = []
    for non_transient_info in zip(non_transient_graphs, non_transient_results):
        non_transient_strings = non_transient_strings + [transient_to_string(False, non_transient_info)]

    # Print out the results strings
    for transient in transient_strings:
        print transient
    for non_transient in non_transient_strings:
        print non_transient


def transient_to_string(isTransient, transient):
    """
    Prints out information about the given possible transient.
    :param isTransient: Whether or not the observations should represent a transient.
    :param transient: The observations and results for the possible transient.
    :return: A string representing the possible transient.
    """
    light_curve = transient[0]
    if isTransient:
        category = "Transient: "
    else:
        category = "Non-Transient: "

    if transient[1] == isTransient:
        category = category + "Success"
    else:
        category = category + "Failure"

    return "----------\n" + str(light_curve) + "\n" + str(category) + "\n"


# CLI options
main.add_param("number", help="set number of test transients", type=int)
main.add_param("-v", "--verbose", default=0, action="count", help="output all observation data and results")

# Run main function
if __name__ == "__main__":
    main.run()
