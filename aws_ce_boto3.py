import boto3

ce = boto3.client('ce')

response = ce.get_cost_and_usage(
    TimePeriod={
        'Start': '2021-11-01',
        'End': '2021-11-30'
    },
    Granularity='MONTHLY',
    Filter={
        'Dimensions': {
            'Key': 'SERVICE',
            'Values': [
                'EC2 - Other'
            ]
        }
    },
    Metrics=[
        'UnblendedCost'
    ],
    GroupBy=[
        {
            'Type': 'TAG',
            'Key': 'Name'
        }
    ]
)

print(response)
