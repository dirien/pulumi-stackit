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
    /// SQLServer Flex user resource schema. Must have a `region` specified in the provider configuration.
    /// 
    /// ## Example Usage
    /// </summary>
    [StackitResourceType("stackit:index/sqlserverflexUser:SqlserverflexUser")]
    public partial class SqlserverflexUser : global::Pulumi.CustomResource
    {
        [Output("host")]
        public Output<string> Host { get; private set; } = null!;

        /// <summary>
        /// ID of the SQLServer Flex instance.
        /// </summary>
        [Output("instanceId")]
        public Output<string> InstanceId { get; private set; } = null!;

        /// <summary>
        /// Password of the user account.
        /// </summary>
        [Output("password")]
        public Output<string> Password { get; private set; } = null!;

        [Output("port")]
        public Output<int> Port { get; private set; } = null!;

        /// <summary>
        /// STACKIT project ID to which the instance is associated.
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// Database access levels for the user. The values for the default roles are: `##STACKIT_DatabaseManager##`, `##STACKIT_LoginManager##`, `##STACKIT_ProcessManager##`, `##STACKIT_ServerManager##`, `##STACKIT_SQLAgentManager##`, `##STACKIT_SQLAgentUser##`
        /// </summary>
        [Output("roles")]
        public Output<ImmutableArray<string>> Roles { get; private set; } = null!;

        /// <summary>
        /// User ID.
        /// </summary>
        [Output("userId")]
        public Output<string> UserId { get; private set; } = null!;

        /// <summary>
        /// Username of the SQLServer Flex instance.
        /// </summary>
        [Output("username")]
        public Output<string> Username { get; private set; } = null!;


        /// <summary>
        /// Create a SqlserverflexUser resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SqlserverflexUser(string name, SqlserverflexUserArgs args, CustomResourceOptions? options = null)
            : base("stackit:index/sqlserverflexUser:SqlserverflexUser", name, args ?? new SqlserverflexUserArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SqlserverflexUser(string name, Input<string> id, SqlserverflexUserState? state = null, CustomResourceOptions? options = null)
            : base("stackit:index/sqlserverflexUser:SqlserverflexUser", name, state, MakeResourceOptions(options, id))
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
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing SqlserverflexUser resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SqlserverflexUser Get(string name, Input<string> id, SqlserverflexUserState? state = null, CustomResourceOptions? options = null)
        {
            return new SqlserverflexUser(name, id, state, options);
        }
    }

    public sealed class SqlserverflexUserArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the SQLServer Flex instance.
        /// </summary>
        [Input("instanceId", required: true)]
        public Input<string> InstanceId { get; set; } = null!;

        /// <summary>
        /// STACKIT project ID to which the instance is associated.
        /// </summary>
        [Input("projectId", required: true)]
        public Input<string> ProjectId { get; set; } = null!;

        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("roles")]
        private InputList<string>? _roles;

        /// <summary>
        /// Database access levels for the user. The values for the default roles are: `##STACKIT_DatabaseManager##`, `##STACKIT_LoginManager##`, `##STACKIT_ProcessManager##`, `##STACKIT_ServerManager##`, `##STACKIT_SQLAgentManager##`, `##STACKIT_SQLAgentUser##`
        /// </summary>
        public InputList<string> Roles
        {
            get => _roles ?? (_roles = new InputList<string>());
            set => _roles = value;
        }

        /// <summary>
        /// Username of the SQLServer Flex instance.
        /// </summary>
        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        public SqlserverflexUserArgs()
        {
        }
        public static new SqlserverflexUserArgs Empty => new SqlserverflexUserArgs();
    }

    public sealed class SqlserverflexUserState : global::Pulumi.ResourceArgs
    {
        [Input("host")]
        public Input<string>? Host { get; set; }

        /// <summary>
        /// ID of the SQLServer Flex instance.
        /// </summary>
        [Input("instanceId")]
        public Input<string>? InstanceId { get; set; }

        [Input("password")]
        private Input<string>? _password;

        /// <summary>
        /// Password of the user account.
        /// </summary>
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
        /// STACKIT project ID to which the instance is associated.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("roles")]
        private InputList<string>? _roles;

        /// <summary>
        /// Database access levels for the user. The values for the default roles are: `##STACKIT_DatabaseManager##`, `##STACKIT_LoginManager##`, `##STACKIT_ProcessManager##`, `##STACKIT_ServerManager##`, `##STACKIT_SQLAgentManager##`, `##STACKIT_SQLAgentUser##`
        /// </summary>
        public InputList<string> Roles
        {
            get => _roles ?? (_roles = new InputList<string>());
            set => _roles = value;
        }

        /// <summary>
        /// User ID.
        /// </summary>
        [Input("userId")]
        public Input<string>? UserId { get; set; }

        /// <summary>
        /// Username of the SQLServer Flex instance.
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public SqlserverflexUserState()
        {
        }
        public static new SqlserverflexUserState Empty => new SqlserverflexUserState();
    }
}
