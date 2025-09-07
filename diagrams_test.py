from diagrams import Diagram
from diagrams.aws.network import APIGateway, ALB, Route53, CloudFront
from diagrams.programming.framework import NextJs
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.analytics import AmazonOpensearchService

with Diagram(None, show=False, graph_attr={"pad": "1"}):
    gw = APIGateway("API Gateway")
    lb = ALB("Load Balancer")
    cf = CloudFront("CloudFront")
    Route53("DNS") >> cf
    cf >> lb
    cf >> gw
    lb >> NextJs("UI")
    gw >> Lambda("Auth Service") >> Dynamodb("Auth DB")
    gw >> Lambda("Blog Service") >> Dynamodb("Blog DB")
    gw >> Lambda("Analytics Service") >> AmazonOpensearchService("OpenSearch")
