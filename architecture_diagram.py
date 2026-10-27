from diagrams import Diagram, Edge, Cluster
from diagrams.aws.devtools import CLI
from diagrams.aws.security import IAM
from diagrams.aws.storage import S3
from diagrams.programming.language import Python

graph_attr = {"ranksep": "2.0", "nodesep": "1.0", "labelloc": "t", "pad": "0.5"}

with Diagram("AWS-scanner", show=False, direction="LR",
filename="aws_scanner_architecture", graph_attr=graph_attr):

    with Cluster("Your machine"):
        app = Python("AWS scanner\n(read-only key)")
        terminal = CLI("PASS/FAIL")

    with Cluster("AWS account"):
        bucket = S3("S3 buckets")
        iam_node = IAM("IAM")

    app >> Edge(label="Block Public Access flags\nbucket encryption",
                forward=True, reverse=True) >> bucket
    app >> Edge(label="root MFA\naccess keys",
                forward=True, reverse=True) >> iam_node
    app >> Edge(label="results", constraint="false") >> terminal

