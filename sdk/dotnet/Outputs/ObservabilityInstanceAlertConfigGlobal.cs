// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Stackit.Outputs
{

    [OutputType]
    public sealed class ObservabilityInstanceAlertConfigGlobal
    {
        /// <summary>
        /// The API key for OpsGenie.
        /// </summary>
        public readonly string? OpsgenieApiKey;
        /// <summary>
        /// The host to send OpsGenie API requests to. Must be a valid URL
        /// </summary>
        public readonly string? OpsgenieApiUrl;
        /// <summary>
        /// The default value used by alertmanager if the alert does not include EndsAt. After this time passes, it can declare the alert as resolved if it has not been updated. This has no impact on alerts from Prometheus, as they always include EndsAt.
        /// </summary>
        public readonly string? ResolveTimeout;
        /// <summary>
        /// SMTP authentication information. Must be a valid email address
        /// </summary>
        public readonly string? SmtpAuthIdentity;
        /// <summary>
        /// SMTP Auth using LOGIN and PLAIN.
        /// </summary>
        public readonly string? SmtpAuthPassword;
        /// <summary>
        /// SMTP Auth using CRAM-MD5, LOGIN and PLAIN. If empty, Alertmanager doesn't authenticate to the SMTP server.
        /// </summary>
        public readonly string? SmtpAuthUsername;
        /// <summary>
        /// The default SMTP From header field. Must be a valid email address
        /// </summary>
        public readonly string? SmtpFrom;
        /// <summary>
        /// The default SMTP smarthost used for sending emails, including port number in format `host:port` (eg. `smtp.example.com:587`). Port number usually is 25, or 587 for SMTP over TLS (sometimes referred to as STARTTLS).
        /// </summary>
        public readonly string? SmtpSmartHost;

        [OutputConstructor]
        private ObservabilityInstanceAlertConfigGlobal(
            string? opsgenieApiKey,

            string? opsgenieApiUrl,

            string? resolveTimeout,

            string? smtpAuthIdentity,

            string? smtpAuthPassword,

            string? smtpAuthUsername,

            string? smtpFrom,

            string? smtpSmartHost)
        {
            OpsgenieApiKey = opsgenieApiKey;
            OpsgenieApiUrl = opsgenieApiUrl;
            ResolveTimeout = resolveTimeout;
            SmtpAuthIdentity = smtpAuthIdentity;
            SmtpAuthPassword = smtpAuthPassword;
            SmtpAuthUsername = smtpAuthUsername;
            SmtpFrom = smtpFrom;
            SmtpSmartHost = smtpSmartHost;
        }
    }
}
