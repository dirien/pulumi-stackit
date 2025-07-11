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
    /// LogMe credential resource schema. Must have a `region` specified in the provider configuration.
    /// 
    /// ## Example Usage
    /// </summary>
    [StackitResourceType("stackit:index/logmeCredential:LogmeCredential")]
    public partial class LogmeCredential : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The credential's ID.
        /// </summary>
        [Output("credentialId")]
        public Output<string> CredentialId { get; private set; } = null!;

        [Output("host")]
        public Output<string> Host { get; private set; } = null!;

        /// <summary>
        /// ID of the LogMe instance.
        /// </summary>
        [Output("instanceId")]
        public Output<string> InstanceId { get; private set; } = null!;

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

        [Output("username")]
        public Output<string> Username { get; private set; } = null!;


        /// <summary>
        /// Create a LogmeCredential resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LogmeCredential(string name, LogmeCredentialArgs args, CustomResourceOptions? options = null)
            : base("stackit:index/logmeCredential:LogmeCredential", name, args ?? new LogmeCredentialArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LogmeCredential(string name, Input<string> id, LogmeCredentialState? state = null, CustomResourceOptions? options = null)
            : base("stackit:index/logmeCredential:LogmeCredential", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing LogmeCredential resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LogmeCredential Get(string name, Input<string> id, LogmeCredentialState? state = null, CustomResourceOptions? options = null)
        {
            return new LogmeCredential(name, id, state, options);
        }
    }

    public sealed class LogmeCredentialArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the LogMe instance.
        /// </summary>
        [Input("instanceId", required: true)]
        public Input<string> InstanceId { get; set; } = null!;

        /// <summary>
        /// STACKIT Project ID to which the instance is associated.
        /// </summary>
        [Input("projectId", required: true)]
        public Input<string> ProjectId { get; set; } = null!;

        public LogmeCredentialArgs()
        {
        }
        public static new LogmeCredentialArgs Empty => new LogmeCredentialArgs();
    }

    public sealed class LogmeCredentialState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The credential's ID.
        /// </summary>
        [Input("credentialId")]
        public Input<string>? CredentialId { get; set; }

        [Input("host")]
        public Input<string>? Host { get; set; }

        /// <summary>
        /// ID of the LogMe instance.
        /// </summary>
        [Input("instanceId")]
        public Input<string>? InstanceId { get; set; }

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

        [Input("username")]
        public Input<string>? Username { get; set; }

        public LogmeCredentialState()
        {
        }
        public static new LogmeCredentialState Empty => new LogmeCredentialState();
    }
}
