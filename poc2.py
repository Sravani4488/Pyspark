import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Data Catalog table
DataCatalogtable_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="finaldb",
    table_name="transform",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        (
            "_96035_addressverificationca_verification_status",
            "long",
            "_96035_addressverificationca_verification_status",
            "long",
        ),
        ("accountgroup", "string", "accountgroup", "string"),
        ("addressline1", "string", "addressline1", "string"),
        ("addressline2", "string", "addressline2", "string"),
        ("addressline3", "string", "addressline3", "string"),
        ("approved_count", "string", "approved_count", "string"),
        ("businessnumber", "string", "businessnumber", "string"),
        ("candelete", "boolean", "candelete", "boolean"),
        ("canupdate", "boolean", "canupdate", "boolean"),
        ("city", "string", "city", "string"),
        ("code", "long", "code", "long"),
        ("companytype", "string", "companytype", "string"),
        ("country", "string", "country", "string"),
        ("emailaddress", "string", "emailaddress", "string"),
        ("enterdtm", "string", "enterdtm", "string"),
        ("enterusername", "string", "enterusername", "string"),
        ("golden_record", "string", "golden_record", "string"),
        ("id", "string", "id", "string"),
        ("internalid", "long", "internalid", "long"),
        ("jdedwardaccountid", "long", "jdedwardaccountid", "long"),
        ("lastchgdtm", "string", "lastchgdtm", "string"),
        ("lastchgusername", "string", "lastchgusername", "string"),
        ("latitude", "double", "latitude", "double"),
        ("location_confidence", "long", "location_confidence", "long"),
        ("location_response_count", "double", "location_response_count", "double"),
        (
            "location_verification_status",
            "long",
            "location_verification_status",
            "long",
        ),
        ("longitude", "double", "longitude", "double"),
        ("match_cluster", "long", "match_cluster", "long"),
        ("match_datetime", "string", "match_datetime", "string"),
        ("match_member", "long", "match_member", "long"),
        ("match_multigroup", "long", "match_multigroup", "long"),
        ("match_status", "long", "match_status", "long"),
        ("match_strategy", "string", "match_strategy", "string"),
        ("match_user", "string", "match_user", "string"),
        ("model_confidence", "double", "model_confidence", "double"),
        ("name", "string", "name", "string"),
        ("phonenumber", "string", "phonenumber", "string"),
        ("postalcode", "string", "postalcode", "string"),
        ("proposed_count", "string", "proposed_count", "string"),
        ("sales", "long", "sales", "long"),
        ("segment", "string", "segment", "string"),
        ("sourcecode", "long", "sourcecode", "long"),
        ("sourcesystem", "string", "sourcesystem", "string"),
        ("stateprovince", "string", "stateprovince", "string"),
        ("status", "string", "status", "string"),
        ("std_address", "string", "std_address", "string"),
        ("std_city", "string", "std_city", "string"),
        ("std_country", "string", "std_country", "string"),
        ("std_country_code", "string", "std_country_code", "string"),
        ("std_county", "string", "std_county", "string"),
        ("std_full_address", "string", "std_full_address", "string"),
        ("std_state", "string", "std_state", "string"),
        ("std_zip", "string", "std_zip", "string"),
        ("validationstatusid", "long", "validationstatusid", "long"),
        ("website", "string", "website", "string"),
        ("zendeskaccountid", "long", "zendeskaccountid", "long"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node Amazon Redshift
AmazonRedshift_node3 = glueContext.write_dynamic_frame.from_options(
    frame=ApplyMapping_node2,
    connection_type="redshift",
    connection_options={
        "redshiftTmpDir": "s3://aws-glue-assets-462533425464-eu-north-1/temporary/",
        "useConnectionProperties": "true",
        "dbtable": "public.susheeldemo",
        "connectionName": "myredshiftconnection",
        "preactions": "CREATE TABLE IF NOT EXISTS public.susheeldemo (_96035_addressverificationca_verification_status BIGINT, accountgroup VARCHAR, addressline1 VARCHAR, addressline2 VARCHAR, addressline3 VARCHAR, approved_count VARCHAR, businessnumber VARCHAR, candelete BOOLEAN, canupdate BOOLEAN, city VARCHAR, code BIGINT, companytype VARCHAR, country VARCHAR, emailaddress VARCHAR, enterdtm VARCHAR, enterusername VARCHAR, golden_record VARCHAR, id VARCHAR, internalid BIGINT, jdedwardaccountid BIGINT, lastchgdtm VARCHAR, lastchgusername VARCHAR, latitude DOUBLE PRECISION, location_confidence BIGINT, location_response_count DOUBLE PRECISION, location_verification_status BIGINT, longitude DOUBLE PRECISION, match_cluster BIGINT, match_datetime VARCHAR, match_member BIGINT, match_multigroup BIGINT, match_status BIGINT, match_strategy VARCHAR, match_user VARCHAR, model_confidence DOUBLE PRECISION, name VARCHAR, phonenumber VARCHAR, postalcode VARCHAR, proposed_count VARCHAR, sales BIGINT, segment VARCHAR, sourcecode BIGINT, sourcesystem VARCHAR, stateprovince VARCHAR, status VARCHAR, std_address VARCHAR, std_city VARCHAR, std_country VARCHAR, std_country_code VARCHAR, std_county VARCHAR, std_full_address VARCHAR, std_state VARCHAR, std_zip VARCHAR, validationstatusid BIGINT, website VARCHAR, zendeskaccountid BIGINT); TRUNCATE TABLE public.susheeldemo;",
    },
    transformation_ctx="AmazonRedshift_node3",
)

job.commit()
