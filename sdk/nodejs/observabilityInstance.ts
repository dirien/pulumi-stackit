// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Observability instance resource schema. Must have a `region` specified in the provider configuration.
 *
 * ## Example Usage
 */
export class ObservabilityInstance extends pulumi.CustomResource {
    /**
     * Get an existing ObservabilityInstance resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ObservabilityInstanceState, opts?: pulumi.CustomResourceOptions): ObservabilityInstance {
        return new ObservabilityInstance(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'stackit:index/observabilityInstance:ObservabilityInstance';

    /**
     * Returns true if the given object is an instance of ObservabilityInstance.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ObservabilityInstance {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ObservabilityInstance.__pulumiType;
    }

    /**
     * The access control list for this instance. Each entry is an IP address range that is permitted to access, in CIDR notation.
     */
    public readonly acls!: pulumi.Output<string[] | undefined>;
    /**
     * Alert configuration for the instance.
     */
    public readonly alertConfig!: pulumi.Output<outputs.ObservabilityInstanceAlertConfig | undefined>;
    /**
     * Specifies Alerting URL.
     */
    public /*out*/ readonly alertingUrl!: pulumi.Output<string>;
    /**
     * Specifies Observability instance dashboard URL.
     */
    public /*out*/ readonly dashboardUrl!: pulumi.Output<string>;
    /**
     * Specifies an initial Grafana admin password.
     */
    public /*out*/ readonly grafanaInitialAdminPassword!: pulumi.Output<string>;
    /**
     * Specifies an initial Grafana admin username.
     */
    public /*out*/ readonly grafanaInitialAdminUser!: pulumi.Output<string>;
    /**
     * If true, anyone can access Grafana dashboards without logging in.
     */
    public /*out*/ readonly grafanaPublicReadAccess!: pulumi.Output<boolean>;
    /**
     * Specifies Grafana URL.
     */
    public /*out*/ readonly grafanaUrl!: pulumi.Output<string>;
    /**
     * The Observability instance ID.
     */
    public /*out*/ readonly instanceId!: pulumi.Output<string>;
    /**
     * Specifies if the instance can be updated.
     */
    public /*out*/ readonly isUpdatable!: pulumi.Output<boolean>;
    public /*out*/ readonly jaegerTracesUrl!: pulumi.Output<string>;
    public /*out*/ readonly jaegerUiUrl!: pulumi.Output<string>;
    /**
     * Specifies URL for pushing logs.
     */
    public /*out*/ readonly logsPushUrl!: pulumi.Output<string>;
    /**
     * Specifies Logs URL.
     */
    public /*out*/ readonly logsUrl!: pulumi.Output<string>;
    /**
     * Specifies URL for pushing metrics.
     */
    public /*out*/ readonly metricsPushUrl!: pulumi.Output<string>;
    /**
     * Specifies for how many days the raw metrics are kept.
     */
    public readonly metricsRetentionDays!: pulumi.Output<number>;
    /**
     * Specifies for how many days the 1h downsampled metrics are kept. must be less than the value of the 5m downsampling retention. Default is set to `0` (disabled).
     */
    public readonly metricsRetentionDays1hDownsampling!: pulumi.Output<number>;
    /**
     * Specifies for how many days the 5m downsampled metrics are kept. must be less than the value of the general retention. Default is set to `0` (disabled).
     */
    public readonly metricsRetentionDays5mDownsampling!: pulumi.Output<number>;
    /**
     * Specifies metrics URL.
     */
    public /*out*/ readonly metricsUrl!: pulumi.Output<string>;
    /**
     * The name of the Observability instance.
     */
    public readonly name!: pulumi.Output<string>;
    public /*out*/ readonly otlpTracesUrl!: pulumi.Output<string>;
    /**
     * Additional parameters.
     */
    public readonly parameters!: pulumi.Output<{[key: string]: string}>;
    /**
     * The Observability plan ID.
     */
    public /*out*/ readonly planId!: pulumi.Output<string>;
    /**
     * Specifies the Observability plan. E.g. `Observability-Monitoring-Medium-EU01`.
     */
    public readonly planName!: pulumi.Output<string>;
    /**
     * STACKIT project ID to which the instance is associated.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * Specifies Targets URL.
     */
    public /*out*/ readonly targetsUrl!: pulumi.Output<string>;
    public /*out*/ readonly zipkinSpansUrl!: pulumi.Output<string>;

    /**
     * Create a ObservabilityInstance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ObservabilityInstanceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ObservabilityInstanceArgs | ObservabilityInstanceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ObservabilityInstanceState | undefined;
            resourceInputs["acls"] = state ? state.acls : undefined;
            resourceInputs["alertConfig"] = state ? state.alertConfig : undefined;
            resourceInputs["alertingUrl"] = state ? state.alertingUrl : undefined;
            resourceInputs["dashboardUrl"] = state ? state.dashboardUrl : undefined;
            resourceInputs["grafanaInitialAdminPassword"] = state ? state.grafanaInitialAdminPassword : undefined;
            resourceInputs["grafanaInitialAdminUser"] = state ? state.grafanaInitialAdminUser : undefined;
            resourceInputs["grafanaPublicReadAccess"] = state ? state.grafanaPublicReadAccess : undefined;
            resourceInputs["grafanaUrl"] = state ? state.grafanaUrl : undefined;
            resourceInputs["instanceId"] = state ? state.instanceId : undefined;
            resourceInputs["isUpdatable"] = state ? state.isUpdatable : undefined;
            resourceInputs["jaegerTracesUrl"] = state ? state.jaegerTracesUrl : undefined;
            resourceInputs["jaegerUiUrl"] = state ? state.jaegerUiUrl : undefined;
            resourceInputs["logsPushUrl"] = state ? state.logsPushUrl : undefined;
            resourceInputs["logsUrl"] = state ? state.logsUrl : undefined;
            resourceInputs["metricsPushUrl"] = state ? state.metricsPushUrl : undefined;
            resourceInputs["metricsRetentionDays"] = state ? state.metricsRetentionDays : undefined;
            resourceInputs["metricsRetentionDays1hDownsampling"] = state ? state.metricsRetentionDays1hDownsampling : undefined;
            resourceInputs["metricsRetentionDays5mDownsampling"] = state ? state.metricsRetentionDays5mDownsampling : undefined;
            resourceInputs["metricsUrl"] = state ? state.metricsUrl : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["otlpTracesUrl"] = state ? state.otlpTracesUrl : undefined;
            resourceInputs["parameters"] = state ? state.parameters : undefined;
            resourceInputs["planId"] = state ? state.planId : undefined;
            resourceInputs["planName"] = state ? state.planName : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["targetsUrl"] = state ? state.targetsUrl : undefined;
            resourceInputs["zipkinSpansUrl"] = state ? state.zipkinSpansUrl : undefined;
        } else {
            const args = argsOrState as ObservabilityInstanceArgs | undefined;
            if ((!args || args.planName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'planName'");
            }
            if ((!args || args.projectId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectId'");
            }
            resourceInputs["acls"] = args ? args.acls : undefined;
            resourceInputs["alertConfig"] = args ? args.alertConfig : undefined;
            resourceInputs["metricsRetentionDays"] = args ? args.metricsRetentionDays : undefined;
            resourceInputs["metricsRetentionDays1hDownsampling"] = args ? args.metricsRetentionDays1hDownsampling : undefined;
            resourceInputs["metricsRetentionDays5mDownsampling"] = args ? args.metricsRetentionDays5mDownsampling : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["parameters"] = args ? args.parameters : undefined;
            resourceInputs["planName"] = args ? args.planName : undefined;
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["alertingUrl"] = undefined /*out*/;
            resourceInputs["dashboardUrl"] = undefined /*out*/;
            resourceInputs["grafanaInitialAdminPassword"] = undefined /*out*/;
            resourceInputs["grafanaInitialAdminUser"] = undefined /*out*/;
            resourceInputs["grafanaPublicReadAccess"] = undefined /*out*/;
            resourceInputs["grafanaUrl"] = undefined /*out*/;
            resourceInputs["instanceId"] = undefined /*out*/;
            resourceInputs["isUpdatable"] = undefined /*out*/;
            resourceInputs["jaegerTracesUrl"] = undefined /*out*/;
            resourceInputs["jaegerUiUrl"] = undefined /*out*/;
            resourceInputs["logsPushUrl"] = undefined /*out*/;
            resourceInputs["logsUrl"] = undefined /*out*/;
            resourceInputs["metricsPushUrl"] = undefined /*out*/;
            resourceInputs["metricsUrl"] = undefined /*out*/;
            resourceInputs["otlpTracesUrl"] = undefined /*out*/;
            resourceInputs["planId"] = undefined /*out*/;
            resourceInputs["targetsUrl"] = undefined /*out*/;
            resourceInputs["zipkinSpansUrl"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["grafanaInitialAdminPassword"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(ObservabilityInstance.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ObservabilityInstance resources.
 */
export interface ObservabilityInstanceState {
    /**
     * The access control list for this instance. Each entry is an IP address range that is permitted to access, in CIDR notation.
     */
    acls?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Alert configuration for the instance.
     */
    alertConfig?: pulumi.Input<inputs.ObservabilityInstanceAlertConfig>;
    /**
     * Specifies Alerting URL.
     */
    alertingUrl?: pulumi.Input<string>;
    /**
     * Specifies Observability instance dashboard URL.
     */
    dashboardUrl?: pulumi.Input<string>;
    /**
     * Specifies an initial Grafana admin password.
     */
    grafanaInitialAdminPassword?: pulumi.Input<string>;
    /**
     * Specifies an initial Grafana admin username.
     */
    grafanaInitialAdminUser?: pulumi.Input<string>;
    /**
     * If true, anyone can access Grafana dashboards without logging in.
     */
    grafanaPublicReadAccess?: pulumi.Input<boolean>;
    /**
     * Specifies Grafana URL.
     */
    grafanaUrl?: pulumi.Input<string>;
    /**
     * The Observability instance ID.
     */
    instanceId?: pulumi.Input<string>;
    /**
     * Specifies if the instance can be updated.
     */
    isUpdatable?: pulumi.Input<boolean>;
    jaegerTracesUrl?: pulumi.Input<string>;
    jaegerUiUrl?: pulumi.Input<string>;
    /**
     * Specifies URL for pushing logs.
     */
    logsPushUrl?: pulumi.Input<string>;
    /**
     * Specifies Logs URL.
     */
    logsUrl?: pulumi.Input<string>;
    /**
     * Specifies URL for pushing metrics.
     */
    metricsPushUrl?: pulumi.Input<string>;
    /**
     * Specifies for how many days the raw metrics are kept.
     */
    metricsRetentionDays?: pulumi.Input<number>;
    /**
     * Specifies for how many days the 1h downsampled metrics are kept. must be less than the value of the 5m downsampling retention. Default is set to `0` (disabled).
     */
    metricsRetentionDays1hDownsampling?: pulumi.Input<number>;
    /**
     * Specifies for how many days the 5m downsampled metrics are kept. must be less than the value of the general retention. Default is set to `0` (disabled).
     */
    metricsRetentionDays5mDownsampling?: pulumi.Input<number>;
    /**
     * Specifies metrics URL.
     */
    metricsUrl?: pulumi.Input<string>;
    /**
     * The name of the Observability instance.
     */
    name?: pulumi.Input<string>;
    otlpTracesUrl?: pulumi.Input<string>;
    /**
     * Additional parameters.
     */
    parameters?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The Observability plan ID.
     */
    planId?: pulumi.Input<string>;
    /**
     * Specifies the Observability plan. E.g. `Observability-Monitoring-Medium-EU01`.
     */
    planName?: pulumi.Input<string>;
    /**
     * STACKIT project ID to which the instance is associated.
     */
    projectId?: pulumi.Input<string>;
    /**
     * Specifies Targets URL.
     */
    targetsUrl?: pulumi.Input<string>;
    zipkinSpansUrl?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ObservabilityInstance resource.
 */
export interface ObservabilityInstanceArgs {
    /**
     * The access control list for this instance. Each entry is an IP address range that is permitted to access, in CIDR notation.
     */
    acls?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Alert configuration for the instance.
     */
    alertConfig?: pulumi.Input<inputs.ObservabilityInstanceAlertConfig>;
    /**
     * Specifies for how many days the raw metrics are kept.
     */
    metricsRetentionDays?: pulumi.Input<number>;
    /**
     * Specifies for how many days the 1h downsampled metrics are kept. must be less than the value of the 5m downsampling retention. Default is set to `0` (disabled).
     */
    metricsRetentionDays1hDownsampling?: pulumi.Input<number>;
    /**
     * Specifies for how many days the 5m downsampled metrics are kept. must be less than the value of the general retention. Default is set to `0` (disabled).
     */
    metricsRetentionDays5mDownsampling?: pulumi.Input<number>;
    /**
     * The name of the Observability instance.
     */
    name?: pulumi.Input<string>;
    /**
     * Additional parameters.
     */
    parameters?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Specifies the Observability plan. E.g. `Observability-Monitoring-Medium-EU01`.
     */
    planName: pulumi.Input<string>;
    /**
     * STACKIT project ID to which the instance is associated.
     */
    projectId: pulumi.Input<string>;
}
