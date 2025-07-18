// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Stackit.Inputs
{

    public sealed class ObservabilityInstanceAlertConfigReceiverWebhooksConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Microsoft Teams webhooks require special handling, set this to true if the webhook is for Microsoft Teams.
        /// </summary>
        [Input("msTeams")]
        public Input<bool>? MsTeams { get; set; }

        /// <summary>
        /// The endpoint to send HTTP POST requests to. Must be a valid URL
        /// </summary>
        [Input("url")]
        public Input<string>? Url { get; set; }

        public ObservabilityInstanceAlertConfigReceiverWebhooksConfigArgs()
        {
        }
        public static new ObservabilityInstanceAlertConfigReceiverWebhooksConfigArgs Empty => new ObservabilityInstanceAlertConfigReceiverWebhooksConfigArgs();
    }
}
