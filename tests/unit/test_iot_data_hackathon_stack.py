import aws_cdk as core
import aws_cdk.assertions as assertions

from iot_data_hackathon.iot_data_hackathon_stack import IotDataHackathonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in iot_data_hackathon/iot_data_hackathon_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = IotDataHackathonStack(app, "iot-data-hackathon")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
