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
    public static class GetCdnDistribution
    {
        /// <summary>
        /// CDN distribution data source schema.
        /// 
        /// &gt; This resource is in beta and may be subject to breaking changes in the future. Use with caution. See our guide for how to opt-in to use beta resources.
        /// 
        /// ## Example Usage
        /// 
        /// ```terraform
        /// data "stackit_cdn_distribution" "example" {
        ///   project_id      = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ///   distribution_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        /// }
        /// ```
        /// </summary>
        public static Task<GetCdnDistributionResult> InvokeAsync(GetCdnDistributionArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetCdnDistributionResult>("stackit:index/getCdnDistribution:getCdnDistribution", args ?? new GetCdnDistributionArgs(), options.WithDefaults());

        /// <summary>
        /// CDN distribution data source schema.
        /// 
        /// &gt; This resource is in beta and may be subject to breaking changes in the future. Use with caution. See our guide for how to opt-in to use beta resources.
        /// 
        /// ## Example Usage
        /// 
        /// ```terraform
        /// data "stackit_cdn_distribution" "example" {
        ///   project_id      = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ///   distribution_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        /// }
        /// ```
        /// </summary>
        public static Output<GetCdnDistributionResult> Invoke(GetCdnDistributionInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetCdnDistributionResult>("stackit:index/getCdnDistribution:getCdnDistribution", args ?? new GetCdnDistributionInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// CDN distribution data source schema.
        /// 
        /// &gt; This resource is in beta and may be subject to breaking changes in the future. Use with caution. See our guide for how to opt-in to use beta resources.
        /// 
        /// ## Example Usage
        /// 
        /// ```terraform
        /// data "stackit_cdn_distribution" "example" {
        ///   project_id      = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        ///   distribution_id = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        /// }
        /// ```
        /// </summary>
        public static Output<GetCdnDistributionResult> Invoke(GetCdnDistributionInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetCdnDistributionResult>("stackit:index/getCdnDistribution:getCdnDistribution", args ?? new GetCdnDistributionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCdnDistributionArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// STACKIT project ID associated with the distribution
        /// </summary>
        [Input("distributionId", required: true)]
        public string DistributionId { get; set; } = null!;

        /// <summary>
        /// STACKIT project ID associated with the distribution
        /// </summary>
        [Input("projectId", required: true)]
        public string ProjectId { get; set; } = null!;

        public GetCdnDistributionArgs()
        {
        }
        public static new GetCdnDistributionArgs Empty => new GetCdnDistributionArgs();
    }

    public sealed class GetCdnDistributionInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// STACKIT project ID associated with the distribution
        /// </summary>
        [Input("distributionId", required: true)]
        public Input<string> DistributionId { get; set; } = null!;

        /// <summary>
        /// STACKIT project ID associated with the distribution
        /// </summary>
        [Input("projectId", required: true)]
        public Input<string> ProjectId { get; set; } = null!;

        public GetCdnDistributionInvokeArgs()
        {
        }
        public static new GetCdnDistributionInvokeArgs Empty => new GetCdnDistributionInvokeArgs();
    }


    [OutputType]
    public sealed class GetCdnDistributionResult
    {
        /// <summary>
        /// The distribution configuration
        /// </summary>
        public readonly Outputs.GetCdnDistributionConfigResult Config;
        /// <summary>
        /// Time when the distribution was created
        /// </summary>
        public readonly string CreatedAt;
        /// <summary>
        /// STACKIT project ID associated with the distribution
        /// </summary>
        public readonly string DistributionId;
        /// <summary>
        /// List of configured domains for the distribution
        /// </summary>
        public readonly ImmutableArray<Outputs.GetCdnDistributionDomainResult> Domains;
        /// <summary>
        /// List of distribution errors
        /// </summary>
        public readonly ImmutableArray<string> Errors;
        public readonly string Id;
        /// <summary>
        /// STACKIT project ID associated with the distribution
        /// </summary>
        public readonly string ProjectId;
        /// <summary>
        /// Status of the distribution
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// Time when the distribution was last updated
        /// </summary>
        public readonly string UpdatedAt;

        [OutputConstructor]
        private GetCdnDistributionResult(
            Outputs.GetCdnDistributionConfigResult config,

            string createdAt,

            string distributionId,

            ImmutableArray<Outputs.GetCdnDistributionDomainResult> domains,

            ImmutableArray<string> errors,

            string id,

            string projectId,

            string status,

            string updatedAt)
        {
            Config = config;
            CreatedAt = createdAt;
            DistributionId = distributionId;
            Domains = domains;
            Errors = errors;
            Id = id;
            ProjectId = projectId;
            Status = status;
            UpdatedAt = updatedAt;
        }
    }
}
