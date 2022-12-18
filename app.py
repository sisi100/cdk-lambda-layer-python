import aws_cdk as cdk

app = cdk.App()
stack = cdk.Stack(app, "cdk-lambda-layer-python-stack")

# ここに必要なリソース書く

app.synth()
