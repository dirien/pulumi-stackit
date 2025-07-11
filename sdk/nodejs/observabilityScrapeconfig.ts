// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Observability scrape config resource schema. Must have a `region` specified in the provider configuration.
 *
 * ## Example Usage
 */
export class ObservabilityScrapeconfig extends pulumi.CustomResource {
    /**
     * Get an existing ObservabilityScrapeconfig resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ObservabilityScrapeconfigState, opts?: pulumi.CustomResourceOptions): ObservabilityScrapeconfig {
        return new ObservabilityScrapeconfig(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'stackit:index/observabilityScrapeconfig:ObservabilityScrapeconfig';

    /**
     * Returns true if the given object is an instance of ObservabilityScrapeconfig.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ObservabilityScrapeconfig {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ObservabilityScrapeconfig.__pulumiType;
    }

    /**
     * A basic authentication block.
     */
    public readonly basicAuth!: pulumi.Output<outputs.ObservabilityScrapeconfigBasicAuth>;
    /**
     * Observability instance ID to which the scraping job is associated.
     */
    public readonly instanceId!: pulumi.Output<string>;
    /**
     * Specifies the job scraping url path. E.g. `/metrics`.
     */
    public readonly metricsPath!: pulumi.Output<string>;
    /**
     * Specifies the name of the scraping job.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * STACKIT project ID to which the scraping job is associated.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * A SAML2 configuration block.
     */
    public readonly saml2!: pulumi.Output<outputs.ObservabilityScrapeconfigSaml2>;
    /**
     * Specifies the scrape sample limit. Upper limit depends on the service plan. Defaults to `5000`.
     */
    public readonly sampleLimit!: pulumi.Output<number>;
    /**
     * Specifies the http scheme. Defaults to `https`.
     */
    public readonly scheme!: pulumi.Output<string>;
    /**
     * Specifies the scrape interval as duration string. Defaults to `5m`.
     */
    public readonly scrapeInterval!: pulumi.Output<string>;
    /**
     * Specifies the scrape timeout as duration string. Defaults to `2m`.
     */
    public readonly scrapeTimeout!: pulumi.Output<string>;
    /**
     * The targets list (specified by the static config).
     */
    public readonly targets!: pulumi.Output<outputs.ObservabilityScrapeconfigTarget[]>;

    /**
     * Create a ObservabilityScrapeconfig resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ObservabilityScrapeconfigArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ObservabilityScrapeconfigArgs | ObservabilityScrapeconfigState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ObservabilityScrapeconfigState | undefined;
            resourceInputs["basicAuth"] = state ? state.basicAuth : undefined;
            resourceInputs["instanceId"] = state ? state.instanceId : undefined;
            resourceInputs["metricsPath"] = state ? state.metricsPath : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["saml2"] = state ? state.saml2 : undefined;
            resourceInputs["sampleLimit"] = state ? state.sampleLimit : undefined;
            resourceInputs["scheme"] = state ? state.scheme : undefined;
            resourceInputs["scrapeInterval"] = state ? state.scrapeInterval : undefined;
            resourceInputs["scrapeTimeout"] = state ? state.scrapeTimeout : undefined;
            resourceInputs["targets"] = state ? state.targets : undefined;
        } else {
            const args = argsOrState as ObservabilityScrapeconfigArgs | undefined;
            if ((!args || args.instanceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceId'");
            }
            if ((!args || args.metricsPath === undefined) && !opts.urn) {
                throw new Error("Missing required property 'metricsPath'");
            }
            if ((!args || args.projectId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectId'");
            }
            if ((!args || args.targets === undefined) && !opts.urn) {
                throw new Error("Missing required property 'targets'");
            }
            resourceInputs["basicAuth"] = args ? args.basicAuth : undefined;
            resourceInputs["instanceId"] = args ? args.instanceId : undefined;
            resourceInputs["metricsPath"] = args ? args.metricsPath : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["saml2"] = args ? args.saml2 : undefined;
            resourceInputs["sampleLimit"] = args ? args.sampleLimit : undefined;
            resourceInputs["scheme"] = args ? args.scheme : undefined;
            resourceInputs["scrapeInterval"] = args ? args.scrapeInterval : undefined;
            resourceInputs["scrapeTimeout"] = args ? args.scrapeTimeout : undefined;
            resourceInputs["targets"] = args ? args.targets : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ObservabilityScrapeconfig.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ObservabilityScrapeconfig resources.
 */
export interface ObservabilityScrapeconfigState {
    /**
     * A basic authentication block.
     */
    basicAuth?: pulumi.Input<inputs.ObservabilityScrapeconfigBasicAuth>;
    /**
     * Observability instance ID to which the scraping job is associated.
     */
    instanceId?: pulumi.Input<string>;
    /**
     * Specifies the job scraping url path. E.g. `/metrics`.
     */
    metricsPath?: pulumi.Input<string>;
    /**
     * Specifies the name of the scraping job.
     */
    name?: pulumi.Input<string>;
    /**
     * STACKIT project ID to which the scraping job is associated.
     */
    projectId?: pulumi.Input<string>;
    /**
     * A SAML2 configuration block.
     */
    saml2?: pulumi.Input<inputs.ObservabilityScrapeconfigSaml2>;
    /**
     * Specifies the scrape sample limit. Upper limit depends on the service plan. Defaults to `5000`.
     */
    sampleLimit?: pulumi.Input<number>;
    /**
     * Specifies the http scheme. Defaults to `https`.
     */
    scheme?: pulumi.Input<string>;
    /**
     * Specifies the scrape interval as duration string. Defaults to `5m`.
     */
    scrapeInterval?: pulumi.Input<string>;
    /**
     * Specifies the scrape timeout as duration string. Defaults to `2m`.
     */
    scrapeTimeout?: pulumi.Input<string>;
    /**
     * The targets list (specified by the static config).
     */
    targets?: pulumi.Input<pulumi.Input<inputs.ObservabilityScrapeconfigTarget>[]>;
}

/**
 * The set of arguments for constructing a ObservabilityScrapeconfig resource.
 */
export interface ObservabilityScrapeconfigArgs {
    /**
     * A basic authentication block.
     */
    basicAuth?: pulumi.Input<inputs.ObservabilityScrapeconfigBasicAuth>;
    /**
     * Observability instance ID to which the scraping job is associated.
     */
    instanceId: pulumi.Input<string>;
    /**
     * Specifies the job scraping url path. E.g. `/metrics`.
     */
    metricsPath: pulumi.Input<string>;
    /**
     * Specifies the name of the scraping job.
     */
    name?: pulumi.Input<string>;
    /**
     * STACKIT project ID to which the scraping job is associated.
     */
    projectId: pulumi.Input<string>;
    /**
     * A SAML2 configuration block.
     */
    saml2?: pulumi.Input<inputs.ObservabilityScrapeconfigSaml2>;
    /**
     * Specifies the scrape sample limit. Upper limit depends on the service plan. Defaults to `5000`.
     */
    sampleLimit?: pulumi.Input<number>;
    /**
     * Specifies the http scheme. Defaults to `https`.
     */
    scheme?: pulumi.Input<string>;
    /**
     * Specifies the scrape interval as duration string. Defaults to `5m`.
     */
    scrapeInterval?: pulumi.Input<string>;
    /**
     * Specifies the scrape timeout as duration string. Defaults to `2m`.
     */
    scrapeTimeout?: pulumi.Input<string>;
    /**
     * The targets list (specified by the static config).
     */
    targets: pulumi.Input<pulumi.Input<inputs.ObservabilityScrapeconfigTarget>[]>;
}
