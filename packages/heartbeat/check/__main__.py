def main(args):
    """Main entry point of the function.
    Can be customed in project.yml
    """

    from urllib import error, request

    try:
        r = request.urlopen("https://flashflashrevolution.com/zageron", timeout=0.2)
        return {
            "body": {"statusCode": 200, "message": "OK"},
            "statusCode": 200,
        }
    except TimeoutError:
        return {
            "body": {"statusCode": 408, "message": "Request Timeout"},
            "statusCode": 200,
        }
    except error.HTTPError:
        return {
            "body": {"statusCode": 503, "message": "Web Error"},
            "statusCode": 200,
        }
    except error.URLError:
        return {
            "body": {"statusCode": 503, "message": "Timeout"},
            "statusCode": 200,
        }
