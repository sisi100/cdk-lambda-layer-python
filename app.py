import aws_cdk as cdk
from aws_cdk import BundlingOptions, DockerImage
from aws_cdk import aws_lambda as lambda_

app = cdk.App()
stack = cdk.Stack(app, "cdk-lambda-layer-python-stack")

# LambdaLayer
layer = lambda_.LayerVersion(
    stack,
    "layer",
    code=lambda_.Code.from_asset(
        "./runtime/layer",
        bundling=BundlingOptions(
            image=DockerImage(image="public.ecr.aws/sam/build-python3.9:latest-x86_64"),  # imageを指定してbuild する
            # image=lambda_.Runtime.PYTHON_3_9.bundling_image, # これでもOK
            user="root",
            command=[
                "cp -aur . /asset-output",
                "cd /asset-output/python",
                "pip install -r requirements.txt -t .",
            ],
        ),
    ),
    compatible_runtimes=[lambda_.Runtime.PYTHON_3_9],
)

# # function
# lambda_.Function(
#     stack,
#     "function",
#     code=lambda_.Code.from_asset(
#         "runtime/function",
#     ),
#     architecture=lambda_.Architecture.ARM_64,
#     handler="index.handler",
#     layers=[layer],
# )


app.synth()
