def is_compliance_result_whitelisted(result):
    try:
        whitelist_key = os.environ['ComplianceWhitelist']
        if whitelist_key == 'none':
            return False
        bucket_wl = whitelist_key.split("/")[0]
        key_wl = "/".join(whitelist_key.split("/")[1:])
        object_wl = S3_CLIENT.get_object(Bucket=bucket_wl, Key=key_wl)
        whitelist_json = json.loads(object_wl["Body"].read().decode("utf-8"))

        for whitelist_item in whitelist_json["Whitelist"]:
            if whitelist_item["ConfigRuleArn"] == result["ConfigRuleArn"]:
                for whitelisted_resources in whitelist_item["WhitelistedResources"]:
                    if result["ResourceId"] in whitelisted_resources["ResourceIds"]:    
                    and whitelisted_resources["ApprovalTicket"] \
                    and datetime.datetime.today().date() <= datetime.datetime.strptime(whitelisted_resources["ValidUntil"], '%Y-%m-%d').date():
                        print(result["ResourceId"] + " whitelisted for " + result["ConfigRuleArn"] + ".")
                        return True
        return False
    except Exception as ex:
        print("Whitelisting review went wrong: {}".format(str(ex)))
        return False


{
	"Whitelist": [{
			"RuleARN": "arn:aws:config:REGION:ACCOUNT_1:config-rule/config-rule-UUID_OF_THE_RULE_1",
			"WhitelistedResources": [{
					"ResourceIds": [
						"RESOURCE_ID"
					],
					"ApprovalTicket": "OPTIONAL_FIELD",
					"ValidUntil": "2019-06-01"
				}
			]
		}, {
			"RuleARN": "arn:aws:config:REGION:ACCOUNT_2:config-rule/config-rule-UUID_OF_THE_RULE_2",
			"WhitelistedResources": [{
					"ResourceIds": [
						"RESOURCE_ID_1",
                        "RESOURCE_ID_2",
                        "RESOURCE_ID_3"
					],
					"ApprovalTicket": "OPTIONAL_LINK_OR_REFERENCE_NUMBER",
					"ValidUntil": "2019-06-01"
				}
			]
		}],
	"ProcessToWhitelist": "OPTIONAL_LINK_TO_PROCESS"
}

#https://github.com/awslabs/aws-config-engine-for-compliance-as-code/blob/master/rules/ROOT_NO_ACCESS_KEY/ROOT_NO_ACCESS_KEY.py
