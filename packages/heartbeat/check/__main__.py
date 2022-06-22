def main(args):
    """Main entry point of the function.
    Can be customed in project.yml
    """

    import os

    hostname = "flashflashrevolution.com"  # example
    response = os.system("ping -c1 -W1 -t150 " + hostname)

    if response == 0:
        return {
            "body": {"statusCode": 200, "message": "OK"},
            "statusCode": 200,
        }
    else:
        return {
            "body": {"statusCode": 503, "message": "BAD"},
            "statusCode": 200,
        }
