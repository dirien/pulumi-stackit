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
    /// RabbitMQ credential resource schema. Must have a `region` specified in the provider configuration.
    /// 
    /// ## Example Usage
    /// </summary>
    [StackitResourceType("stackit:index/rabbitmqCredential:RabbitmqCredential")]
    public partial class RabbitmqCredential : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The credential's ID.
        /// </summary>
        [Output("credentialId")]
        public Output<string> CredentialId { get; private set; } = null!;

        [Output("host")]
        public Output<string> Host { get; private set; } = null!;

        [Output("hosts")]
        public Output<ImmutableArray<string>> Hosts { get; private set; } = null!;

        [Output("httpApiUri")]
        public Output<string> HttpApiUri { get; private set; } = null!;

        [Output("httpApiUris")]
        public Output<ImmutableArray<string>> HttpApiUris { get; private set; } = null!;

        /// <summary>
        /// ID of the RabbitMQ instance.
        /// </summary>
        [Output("instanceId")]
        public Output<string> InstanceId { get; private set; } = null!;

        [Output("management")]
        public Output<string> Management { get; private set; } = null!;

        [Output("password")]
        public Output<string> Password { get; private set; } = null!;

        [Output("port")]
        public Output<int> Port { get; private set; } = null!;

        /// <summary>
        /// STACKIT Project ID to which the instance is associated.
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        [Output("uri")]
        public Output<string> Uri { get; private set; } = null!;

        [Output("uris")]
        public Output<ImmutableArray<string>> Uris { get; private set; } = null!;

        [Output("username")]
        public Output<string> Username { get; private set; } = null!;


        /// <summary>
        /// Create a RabbitmqCredential resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RabbitmqCredential(string name, RabbitmqCredentialArgs args, CustomResourceOptions? options = null)
            : base("stackit:index/rabbitmqCredential:RabbitmqCredential", name, args ?? new RabbitmqCredentialArgs(), MakeResourceOptions(options, ""))
        {
        }

        private RabbitmqCredential(string name, Input<string> id, RabbitmqCredentialState? state = null, CustomResourceOptions? options = null)
            : base("stackit:index/rabbitmqCredential:RabbitmqCredential", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/dirien/pulumi-stackit",
                AdditionalSecretOutputs =
                {
                    "password",
                    "uri",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing RabbitmqCredential resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RabbitmqCredential Get(string name, Input<string> id, RabbitmqCredentialState? state = null, CustomResourceOptions? options = null)
        {
            return new RabbitmqCredential(name, id, state, options);
        }
    }

    public sealed class RabbitmqCredentialArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the RabbitMQ instance.
        /// </summary>
        [Input("instanceId", required: true)]
        public Input<string> InstanceId { get; set; } = null!;

        /// <summary>
        /// STACKIT Project ID to which the instance is associated.
        /// </summary>
        [Input("projectId", required: true)]
        public Input<string> ProjectId { get; set; } = null!;

        public RabbitmqCredentialArgs()
        {
        }
        public static new RabbitmqCredentialArgs Empty => new RabbitmqCredentialArgs();
    }

    public sealed class RabbitmqCredentialState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The credential's ID.
        /// </summary>
        [Input("credentialId")]
        public Input<string>? CredentialId { get; set; }

        [Input("host")]
        public Input<string>? Host { get; set; }

        [Input("hosts")]
        private InputList<string>? _hosts;
        public InputList<string> Hosts
        {
            get => _hosts ?? (_hosts = new InputList<string>());
            set => _hosts = value;
        }

        [Input("httpApiUri")]
        public Input<string>? HttpApiUri { get; set; }

        [Input("httpApiUris")]
        private InputList<string>? _httpApiUris;
        public InputList<string> HttpApiUris
        {
            get => _httpApiUris ?? (_httpApiUris = new InputList<string>());
            set => _httpApiUris = value;
        }

        /// <summary>
        /// ID of the RabbitMQ instance.
        /// </summary>
        [Input("instanceId")]
        public Input<string>? InstanceId { get; set; }

        [Input("management")]
        public Input<string>? Management { get; set; }

        [Input("password")]
        private Input<string>? _password;
        public Input<string>? Password
        {
            get => _password;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _password = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// STACKIT Project ID to which the instance is associated.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        [Input("uri")]
        private Input<string>? _uri;
        public Input<string>? Uri
        {
            get => _uri;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _uri = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("uris")]
        private InputList<string>? _uris;
        public InputList<string> Uris
        {
            get => _uris ?? (_uris = new InputList<string>());
            set => _uris = value;
        }

        [Input("username")]
        public Input<string>? Username { get; set; }

        public RabbitmqCredentialState()
        {
        }
        public static new RabbitmqCredentialState Empty => new RabbitmqCredentialState();
    }
}
