# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
from . import _utilities
import typing
# Export this package's modules as members:
from .affinity_group import *
from .authorization_organization_role_assignment import *
from .authorization_project_role_assignment import *
from .cdn_custom_domain import *
from .cdn_distribution import *
from .dns_record_set import *
from .dns_zone import *
from .get_affinity_group import *
from .get_cdn_custom_domain import *
from .get_cdn_distribution import *
from .get_dns_record_set import *
from .get_dns_zone import *
from .get_git import *
from .get_image import *
from .get_key_pair import *
from .get_loadbalancer import *
from .get_logme_credential import *
from .get_logme_instance import *
from .get_mariadb_credential import *
from .get_mariadb_instance import *
from .get_mongodbflex_instance import *
from .get_mongodbflex_user import *
from .get_network import *
from .get_network_area import *
from .get_network_area_route import *
from .get_network_interface import *
from .get_objectstorage_bucket import *
from .get_objectstorage_credential import *
from .get_objectstorage_credentials_group import *
from .get_observability_alertgroup import *
from .get_observability_instance import *
from .get_observability_logalertgroup import *
from .get_observability_scrapeconfig import *
from .get_opensearch_credential import *
from .get_opensearch_instance import *
from .get_postgresflex_database import *
from .get_postgresflex_instance import *
from .get_postgresflex_user import *
from .get_public_ip import *
from .get_public_ip_ranges import *
from .get_rabbitmq_credential import *
from .get_rabbitmq_instance import *
from .get_redis_credential import *
from .get_redis_instance import *
from .get_resourcemanager_project import *
from .get_secretsmanager_instance import *
from .get_secretsmanager_user import *
from .get_security_group import *
from .get_security_group_rule import *
from .get_server import *
from .get_server_backup_schedule import *
from .get_server_backup_schedules import *
from .get_server_update_schedule import *
from .get_server_update_schedules import *
from .get_service_account import *
from .get_ske_cluster import *
from .get_sqlserverflex_instance import *
from .get_sqlserverflex_user import *
from .get_volume import *
from .git import *
from .image import *
from .key_pair import *
from .loadbalancer import *
from .loadbalancer_observability_credential import *
from .logme_credential import *
from .logme_instance import *
from .mariadb_credential import *
from .mariadb_instance import *
from .modelserving_token import *
from .mongodbflex_instance import *
from .mongodbflex_user import *
from .network import *
from .network_area import *
from .network_area_route import *
from .network_interface import *
from .objectstorage_bucket import *
from .objectstorage_credential import *
from .objectstorage_credentials_group import *
from .observability_alertgroup import *
from .observability_credential import *
from .observability_instance import *
from .observability_logalertgroup import *
from .observability_scrapeconfig import *
from .opensearch_credential import *
from .opensearch_instance import *
from .postgresflex_database import *
from .postgresflex_instance import *
from .postgresflex_user import *
from .provider import *
from .public_ip import *
from .public_ip_associate import *
from .rabbitmq_credential import *
from .rabbitmq_instance import *
from .redis_credential import *
from .redis_instance import *
from .resourcemanager_project import *
from .secretsmanager_instance import *
from .secretsmanager_user import *
from .security_group import *
from .security_group_rule import *
from .server import *
from .server_backup_schedule import *
from .server_network_interface_attach import *
from .server_service_account_attach import *
from .server_update_schedule import *
from .server_volume_attach import *
from .service_account import *
from .service_account_access_token import *
from .service_account_key import *
from .ske_cluster import *
from .ske_kubeconfig import *
from .sqlserverflex_instance import *
from .sqlserverflex_user import *
from .volume import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import ediri_stackit.config as __config
    config = __config
else:
    config = _utilities.lazy_import('ediri_stackit.config')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "stackit",
  "mod": "index/affinityGroup",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/affinityGroup:AffinityGroup": "AffinityGroup"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/authorizationOrganizationRoleAssignment",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/authorizationOrganizationRoleAssignment:AuthorizationOrganizationRoleAssignment": "AuthorizationOrganizationRoleAssignment"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/authorizationProjectRoleAssignment",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/authorizationProjectRoleAssignment:AuthorizationProjectRoleAssignment": "AuthorizationProjectRoleAssignment"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/cdnCustomDomain",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/cdnCustomDomain:CdnCustomDomain": "CdnCustomDomain"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/cdnDistribution",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/cdnDistribution:CdnDistribution": "CdnDistribution"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/dnsRecordSet",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/dnsRecordSet:DnsRecordSet": "DnsRecordSet"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/dnsZone",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/dnsZone:DnsZone": "DnsZone"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/git",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/git:Git": "Git"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/image",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/image:Image": "Image"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/keyPair",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/keyPair:KeyPair": "KeyPair"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/loadbalancer",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/loadbalancer:Loadbalancer": "Loadbalancer"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/loadbalancerObservabilityCredential",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/loadbalancerObservabilityCredential:LoadbalancerObservabilityCredential": "LoadbalancerObservabilityCredential"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/logmeCredential",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/logmeCredential:LogmeCredential": "LogmeCredential"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/logmeInstance",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/logmeInstance:LogmeInstance": "LogmeInstance"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/mariadbCredential",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/mariadbCredential:MariadbCredential": "MariadbCredential"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/mariadbInstance",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/mariadbInstance:MariadbInstance": "MariadbInstance"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/modelservingToken",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/modelservingToken:ModelservingToken": "ModelservingToken"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/mongodbflexInstance",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/mongodbflexInstance:MongodbflexInstance": "MongodbflexInstance"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/mongodbflexUser",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/mongodbflexUser:MongodbflexUser": "MongodbflexUser"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/network",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/network:Network": "Network"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/networkArea",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/networkArea:NetworkArea": "NetworkArea"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/networkAreaRoute",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/networkAreaRoute:NetworkAreaRoute": "NetworkAreaRoute"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/networkInterface",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/networkInterface:NetworkInterface": "NetworkInterface"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/objectstorageBucket",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/objectstorageBucket:ObjectstorageBucket": "ObjectstorageBucket"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/objectstorageCredential",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/objectstorageCredential:ObjectstorageCredential": "ObjectstorageCredential"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/objectstorageCredentialsGroup",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/objectstorageCredentialsGroup:ObjectstorageCredentialsGroup": "ObjectstorageCredentialsGroup"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/observabilityAlertgroup",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/observabilityAlertgroup:ObservabilityAlertgroup": "ObservabilityAlertgroup"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/observabilityCredential",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/observabilityCredential:ObservabilityCredential": "ObservabilityCredential"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/observabilityInstance",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/observabilityInstance:ObservabilityInstance": "ObservabilityInstance"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/observabilityLogalertgroup",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/observabilityLogalertgroup:ObservabilityLogalertgroup": "ObservabilityLogalertgroup"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/observabilityScrapeconfig",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/observabilityScrapeconfig:ObservabilityScrapeconfig": "ObservabilityScrapeconfig"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/opensearchCredential",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/opensearchCredential:OpensearchCredential": "OpensearchCredential"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/opensearchInstance",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/opensearchInstance:OpensearchInstance": "OpensearchInstance"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/postgresflexDatabase",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/postgresflexDatabase:PostgresflexDatabase": "PostgresflexDatabase"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/postgresflexInstance",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/postgresflexInstance:PostgresflexInstance": "PostgresflexInstance"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/postgresflexUser",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/postgresflexUser:PostgresflexUser": "PostgresflexUser"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/publicIp",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/publicIp:PublicIp": "PublicIp"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/publicIpAssociate",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/publicIpAssociate:PublicIpAssociate": "PublicIpAssociate"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/rabbitmqCredential",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/rabbitmqCredential:RabbitmqCredential": "RabbitmqCredential"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/rabbitmqInstance",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/rabbitmqInstance:RabbitmqInstance": "RabbitmqInstance"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/redisCredential",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/redisCredential:RedisCredential": "RedisCredential"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/redisInstance",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/redisInstance:RedisInstance": "RedisInstance"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/resourcemanagerProject",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/resourcemanagerProject:ResourcemanagerProject": "ResourcemanagerProject"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/secretsmanagerInstance",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/secretsmanagerInstance:SecretsmanagerInstance": "SecretsmanagerInstance"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/secretsmanagerUser",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/secretsmanagerUser:SecretsmanagerUser": "SecretsmanagerUser"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/securityGroup",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/securityGroup:SecurityGroup": "SecurityGroup"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/securityGroupRule",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/securityGroupRule:SecurityGroupRule": "SecurityGroupRule"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/server",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/server:Server": "Server"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/serverBackupSchedule",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/serverBackupSchedule:ServerBackupSchedule": "ServerBackupSchedule"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/serverNetworkInterfaceAttach",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/serverNetworkInterfaceAttach:ServerNetworkInterfaceAttach": "ServerNetworkInterfaceAttach"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/serverServiceAccountAttach",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/serverServiceAccountAttach:ServerServiceAccountAttach": "ServerServiceAccountAttach"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/serverUpdateSchedule",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/serverUpdateSchedule:ServerUpdateSchedule": "ServerUpdateSchedule"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/serverVolumeAttach",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/serverVolumeAttach:ServerVolumeAttach": "ServerVolumeAttach"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/serviceAccount",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/serviceAccount:ServiceAccount": "ServiceAccount"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/serviceAccountAccessToken",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/serviceAccountAccessToken:ServiceAccountAccessToken": "ServiceAccountAccessToken"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/serviceAccountKey",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/serviceAccountKey:ServiceAccountKey": "ServiceAccountKey"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/skeCluster",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/skeCluster:SkeCluster": "SkeCluster"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/skeKubeconfig",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/skeKubeconfig:SkeKubeconfig": "SkeKubeconfig"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/sqlserverflexInstance",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/sqlserverflexInstance:SqlserverflexInstance": "SqlserverflexInstance"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/sqlserverflexUser",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/sqlserverflexUser:SqlserverflexUser": "SqlserverflexUser"
  }
 },
 {
  "pkg": "stackit",
  "mod": "index/volume",
  "fqn": "ediri_stackit",
  "classes": {
   "stackit:index/volume:Volume": "Volume"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "stackit",
  "token": "pulumi:providers:stackit",
  "fqn": "ediri_stackit",
  "class": "Provider"
 }
]
"""
)
