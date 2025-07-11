// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Stackit
{
    /// <summary>
    /// The provider type for the stackit package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [StackitResourceType("pulumi:providers:stackit")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        /// <summary>
        /// Custom endpoint for the Argus service
        /// </summary>
        [Output("argusCustomEndpoint")]
        public Output<string?> ArgusCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the Membership service
        /// </summary>
        [Output("authorizationCustomEndpoint")]
        public Output<string?> AuthorizationCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the CDN service
        /// </summary>
        [Output("cdnCustomEndpoint")]
        public Output<string?> CdnCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Path of JSON from where the credentials are read. Takes precedence over the env var `STACKIT_CREDENTIALS_PATH`. Default
        /// value is `~/.stackit/credentials.json`.
        /// </summary>
        [Output("credentialsPath")]
        public Output<string?> CredentialsPath { get; private set; } = null!;

        /// <summary>
        /// Region will be used as the default location for regional services. Not all services require a region, some are global
        /// </summary>
        [Output("defaultRegion")]
        public Output<string?> DefaultRegion { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the DNS service
        /// </summary>
        [Output("dnsCustomEndpoint")]
        public Output<string?> DnsCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the Git service
        /// </summary>
        [Output("gitCustomEndpoint")]
        public Output<string?> GitCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the IaaS service
        /// </summary>
        [Output("iaasCustomEndpoint")]
        public Output<string?> IaasCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the Load Balancer service
        /// </summary>
        [Output("loadbalancerCustomEndpoint")]
        public Output<string?> LoadbalancerCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the LogMe service
        /// </summary>
        [Output("logmeCustomEndpoint")]
        public Output<string?> LogmeCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the MariaDB service
        /// </summary>
        [Output("mariadbCustomEndpoint")]
        public Output<string?> MariadbCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the AI Model Serving service
        /// </summary>
        [Output("modelservingCustomEndpoint")]
        public Output<string?> ModelservingCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the MongoDB Flex service
        /// </summary>
        [Output("mongodbflexCustomEndpoint")]
        public Output<string?> MongodbflexCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the Object Storage service
        /// </summary>
        [Output("objectstorageCustomEndpoint")]
        public Output<string?> ObjectstorageCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the Observability service
        /// </summary>
        [Output("observabilityCustomEndpoint")]
        public Output<string?> ObservabilityCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the OpenSearch service
        /// </summary>
        [Output("opensearchCustomEndpoint")]
        public Output<string?> OpensearchCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the PostgresFlex service
        /// </summary>
        [Output("postgresflexCustomEndpoint")]
        public Output<string?> PostgresflexCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Private RSA key used for authentication, relevant for the key flow. It takes precedence over the private key that is
        /// included in the service account key.
        /// </summary>
        [Output("privateKey")]
        public Output<string?> PrivateKey { get; private set; } = null!;

        /// <summary>
        /// Path for the private RSA key used for authentication, relevant for the key flow. It takes precedence over the private
        /// key that is included in the service account key.
        /// </summary>
        [Output("privateKeyPath")]
        public Output<string?> PrivateKeyPath { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the RabbitMQ service
        /// </summary>
        [Output("rabbitmqCustomEndpoint")]
        public Output<string?> RabbitmqCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the Redis service
        /// </summary>
        [Output("redisCustomEndpoint")]
        public Output<string?> RedisCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Region will be used as the default location for regional services. Not all services require a region, some are global
        /// </summary>
        [Output("region")]
        public Output<string?> Region { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the Resource Manager service
        /// </summary>
        [Output("resourcemanagerCustomEndpoint")]
        public Output<string?> ResourcemanagerCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the Secrets Manager service
        /// </summary>
        [Output("secretsmanagerCustomEndpoint")]
        public Output<string?> SecretsmanagerCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the Server Backup service
        /// </summary>
        [Output("serverBackupCustomEndpoint")]
        public Output<string?> ServerBackupCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the Server Update service
        /// </summary>
        [Output("serverUpdateCustomEndpoint")]
        public Output<string?> ServerUpdateCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the Service Account service
        /// </summary>
        [Output("serviceAccountCustomEndpoint")]
        public Output<string?> ServiceAccountCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Service account email. It can also be set using the environment variable STACKIT_SERVICE_ACCOUNT_EMAIL. It is required
        /// if you want to use the resource manager project resource.
        /// </summary>
        [Output("serviceAccountEmail")]
        public Output<string?> ServiceAccountEmail { get; private set; } = null!;

        /// <summary>
        /// Service account key used for authentication. If set, the key flow will be used to authenticate all operations.
        /// </summary>
        [Output("serviceAccountKey")]
        public Output<string?> ServiceAccountKey { get; private set; } = null!;

        /// <summary>
        /// Path for the service account key used for authentication. If set, the key flow will be used to authenticate all
        /// operations.
        /// </summary>
        [Output("serviceAccountKeyPath")]
        public Output<string?> ServiceAccountKeyPath { get; private set; } = null!;

        /// <summary>
        /// Token used for authentication. If set, the token flow will be used to authenticate all operations.
        /// </summary>
        [Output("serviceAccountToken")]
        public Output<string?> ServiceAccountToken { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the Service Enablement API
        /// </summary>
        [Output("serviceEnablementCustomEndpoint")]
        public Output<string?> ServiceEnablementCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the Kubernetes Engine (SKE) service
        /// </summary>
        [Output("skeCustomEndpoint")]
        public Output<string?> SkeCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the SQL Server Flex service
        /// </summary>
        [Output("sqlserverflexCustomEndpoint")]
        public Output<string?> SqlserverflexCustomEndpoint { get; private set; } = null!;

        /// <summary>
        /// Custom endpoint for the token API, which is used to request access tokens when using the key flow
        /// </summary>
        [Output("tokenCustomEndpoint")]
        public Output<string?> TokenCustomEndpoint { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, CustomResourceOptions? options = null)
            : base("stackit", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/dirien/pulumi-stackit",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }

        /// <summary>
        /// This function returns a Terraform config object with terraform-namecased keys,to be used with the Terraform Module Provider.
        /// </summary>
        public global::Pulumi.Output<ProviderTerraformConfigResult> TerraformConfig()
            => global::Pulumi.Deployment.Instance.Call<ProviderTerraformConfigResult>("pulumi:providers:stackit/terraformConfig", CallArgs.Empty, this);
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Custom endpoint for the Argus service
        /// </summary>
        [Input("argusCustomEndpoint")]
        public Input<string>? ArgusCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the Membership service
        /// </summary>
        [Input("authorizationCustomEndpoint")]
        public Input<string>? AuthorizationCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the CDN service
        /// </summary>
        [Input("cdnCustomEndpoint")]
        public Input<string>? CdnCustomEndpoint { get; set; }

        /// <summary>
        /// Path of JSON from where the credentials are read. Takes precedence over the env var `STACKIT_CREDENTIALS_PATH`. Default
        /// value is `~/.stackit/credentials.json`.
        /// </summary>
        [Input("credentialsPath")]
        public Input<string>? CredentialsPath { get; set; }

        /// <summary>
        /// Region will be used as the default location for regional services. Not all services require a region, some are global
        /// </summary>
        [Input("defaultRegion")]
        public Input<string>? DefaultRegion { get; set; }

        /// <summary>
        /// Custom endpoint for the DNS service
        /// </summary>
        [Input("dnsCustomEndpoint")]
        public Input<string>? DnsCustomEndpoint { get; set; }

        /// <summary>
        /// Enable beta resources. Default is false.
        /// </summary>
        [Input("enableBetaResources", json: true)]
        public Input<bool>? EnableBetaResources { get; set; }

        [Input("experiments", json: true)]
        private InputList<string>? _experiments;

        /// <summary>
        /// Enables experiments. These are unstable features without official support. More information can be found in the README.
        /// Available Experiments: [iam]
        /// </summary>
        public InputList<string> Experiments
        {
            get => _experiments ?? (_experiments = new InputList<string>());
            set => _experiments = value;
        }

        /// <summary>
        /// Custom endpoint for the Git service
        /// </summary>
        [Input("gitCustomEndpoint")]
        public Input<string>? GitCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the IaaS service
        /// </summary>
        [Input("iaasCustomEndpoint")]
        public Input<string>? IaasCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the Load Balancer service
        /// </summary>
        [Input("loadbalancerCustomEndpoint")]
        public Input<string>? LoadbalancerCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the LogMe service
        /// </summary>
        [Input("logmeCustomEndpoint")]
        public Input<string>? LogmeCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the MariaDB service
        /// </summary>
        [Input("mariadbCustomEndpoint")]
        public Input<string>? MariadbCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the AI Model Serving service
        /// </summary>
        [Input("modelservingCustomEndpoint")]
        public Input<string>? ModelservingCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the MongoDB Flex service
        /// </summary>
        [Input("mongodbflexCustomEndpoint")]
        public Input<string>? MongodbflexCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the Object Storage service
        /// </summary>
        [Input("objectstorageCustomEndpoint")]
        public Input<string>? ObjectstorageCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the Observability service
        /// </summary>
        [Input("observabilityCustomEndpoint")]
        public Input<string>? ObservabilityCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the OpenSearch service
        /// </summary>
        [Input("opensearchCustomEndpoint")]
        public Input<string>? OpensearchCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the PostgresFlex service
        /// </summary>
        [Input("postgresflexCustomEndpoint")]
        public Input<string>? PostgresflexCustomEndpoint { get; set; }

        /// <summary>
        /// Private RSA key used for authentication, relevant for the key flow. It takes precedence over the private key that is
        /// included in the service account key.
        /// </summary>
        [Input("privateKey")]
        public Input<string>? PrivateKey { get; set; }

        /// <summary>
        /// Path for the private RSA key used for authentication, relevant for the key flow. It takes precedence over the private
        /// key that is included in the service account key.
        /// </summary>
        [Input("privateKeyPath")]
        public Input<string>? PrivateKeyPath { get; set; }

        /// <summary>
        /// Custom endpoint for the RabbitMQ service
        /// </summary>
        [Input("rabbitmqCustomEndpoint")]
        public Input<string>? RabbitmqCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the Redis service
        /// </summary>
        [Input("redisCustomEndpoint")]
        public Input<string>? RedisCustomEndpoint { get; set; }

        /// <summary>
        /// Region will be used as the default location for regional services. Not all services require a region, some are global
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Custom endpoint for the Resource Manager service
        /// </summary>
        [Input("resourcemanagerCustomEndpoint")]
        public Input<string>? ResourcemanagerCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the Secrets Manager service
        /// </summary>
        [Input("secretsmanagerCustomEndpoint")]
        public Input<string>? SecretsmanagerCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the Server Backup service
        /// </summary>
        [Input("serverBackupCustomEndpoint")]
        public Input<string>? ServerBackupCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the Server Update service
        /// </summary>
        [Input("serverUpdateCustomEndpoint")]
        public Input<string>? ServerUpdateCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the Service Account service
        /// </summary>
        [Input("serviceAccountCustomEndpoint")]
        public Input<string>? ServiceAccountCustomEndpoint { get; set; }

        /// <summary>
        /// Service account email. It can also be set using the environment variable STACKIT_SERVICE_ACCOUNT_EMAIL. It is required
        /// if you want to use the resource manager project resource.
        /// </summary>
        [Input("serviceAccountEmail")]
        public Input<string>? ServiceAccountEmail { get; set; }

        /// <summary>
        /// Service account key used for authentication. If set, the key flow will be used to authenticate all operations.
        /// </summary>
        [Input("serviceAccountKey")]
        public Input<string>? ServiceAccountKey { get; set; }

        /// <summary>
        /// Path for the service account key used for authentication. If set, the key flow will be used to authenticate all
        /// operations.
        /// </summary>
        [Input("serviceAccountKeyPath")]
        public Input<string>? ServiceAccountKeyPath { get; set; }

        /// <summary>
        /// Token used for authentication. If set, the token flow will be used to authenticate all operations.
        /// </summary>
        [Input("serviceAccountToken")]
        public Input<string>? ServiceAccountToken { get; set; }

        /// <summary>
        /// Custom endpoint for the Service Enablement API
        /// </summary>
        [Input("serviceEnablementCustomEndpoint")]
        public Input<string>? ServiceEnablementCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the Kubernetes Engine (SKE) service
        /// </summary>
        [Input("skeCustomEndpoint")]
        public Input<string>? SkeCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the SQL Server Flex service
        /// </summary>
        [Input("sqlserverflexCustomEndpoint")]
        public Input<string>? SqlserverflexCustomEndpoint { get; set; }

        /// <summary>
        /// Custom endpoint for the token API, which is used to request access tokens when using the key flow
        /// </summary>
        [Input("tokenCustomEndpoint")]
        public Input<string>? TokenCustomEndpoint { get; set; }

        public ProviderArgs()
        {
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }

    /// <summary>
    /// The results of the <see cref="Provider.TerraformConfig"/> method.
    /// </summary>
    [OutputType]
    public sealed class ProviderTerraformConfigResult
    {
        public readonly ImmutableDictionary<string, object> Result;

        [OutputConstructor]
        private ProviderTerraformConfigResult(ImmutableDictionary<string, object> result)
        {
            Result = result;
        }
    }
}
