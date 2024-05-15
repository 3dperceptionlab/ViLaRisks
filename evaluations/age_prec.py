"""
Script to get precision of scene detection

Usage: 
    scene_prec.py <predictionFile> <gtFile>

Options:
    -h --help            Show this screen.
    <predictionFile>     Path to the file containing the predictions.
    <gtFile>             Path to the file containing the ground truth.
"""

from docopt import docopt

args = docopt(__doc__)

with open(args['<predictionFile>'], 'r') as predFile:
    predLines = predFile.readlines()
    predLines = [x.strip() for x in predLines]
    predAges = [x.split(',')[1] for x in predLines]

with open(args['<gtFile>'], 'r') as gtFile:
    gtLines = gtFile.readlines()
    gtLines = [x.strip() for x in gtLines]
    gtAges = [x.split(',')[1] for x in gtLines]


score = sum(pred == gt for pred, gt in zip(predAges, gtAges)) / len(gtAges)
print("Precision: {}%".format(round(score * 100, 4)))
    