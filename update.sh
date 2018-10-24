#!/bin/bash
java -jar ../swagger-codegen/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate -i https://api.mailslurp.com/v2/api-docs -l python -DpackageName=mailslurp_api --git-user-id tobias-reese --git-repo-id mailslurp-api -o .
