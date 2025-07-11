// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * SKE kubeconfig resource schema. Must have a `region` specified in the provider configuration.
 *
 * ## Example Usage
 */
export class SkeKubeconfig extends pulumi.CustomResource {
    /**
     * Get an existing SkeKubeconfig resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SkeKubeconfigState, opts?: pulumi.CustomResourceOptions): SkeKubeconfig {
        return new SkeKubeconfig(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'stackit:index/skeKubeconfig:SkeKubeconfig';

    /**
     * Returns true if the given object is an instance of SkeKubeconfig.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SkeKubeconfig {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SkeKubeconfig.__pulumiType;
    }

    /**
     * Name of the SKE cluster.
     */
    public readonly clusterName!: pulumi.Output<string>;
    /**
     * Date-time when the kubeconfig was created
     */
    public /*out*/ readonly creationTime!: pulumi.Output<string>;
    /**
     * Expiration time of the kubeconfig, in seconds. Defaults to `3600`
     */
    public readonly expiration!: pulumi.Output<number>;
    /**
     * Timestamp when the kubeconfig expires
     */
    public /*out*/ readonly expiresAt!: pulumi.Output<string>;
    /**
     * Raw short-lived admin kubeconfig.
     */
    public /*out*/ readonly kubeConfig!: pulumi.Output<string>;
    public /*out*/ readonly kubeConfigId!: pulumi.Output<string>;
    /**
     * STACKIT project ID to which the cluster is associated.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * If set to true, the provider will check if the kubeconfig has expired and will generated a new valid one in-place
     */
    public readonly refresh!: pulumi.Output<boolean | undefined>;

    /**
     * Create a SkeKubeconfig resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SkeKubeconfigArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SkeKubeconfigArgs | SkeKubeconfigState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SkeKubeconfigState | undefined;
            resourceInputs["clusterName"] = state ? state.clusterName : undefined;
            resourceInputs["creationTime"] = state ? state.creationTime : undefined;
            resourceInputs["expiration"] = state ? state.expiration : undefined;
            resourceInputs["expiresAt"] = state ? state.expiresAt : undefined;
            resourceInputs["kubeConfig"] = state ? state.kubeConfig : undefined;
            resourceInputs["kubeConfigId"] = state ? state.kubeConfigId : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["refresh"] = state ? state.refresh : undefined;
        } else {
            const args = argsOrState as SkeKubeconfigArgs | undefined;
            if ((!args || args.clusterName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterName'");
            }
            if ((!args || args.projectId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectId'");
            }
            resourceInputs["clusterName"] = args ? args.clusterName : undefined;
            resourceInputs["expiration"] = args ? args.expiration : undefined;
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["refresh"] = args ? args.refresh : undefined;
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["expiresAt"] = undefined /*out*/;
            resourceInputs["kubeConfig"] = undefined /*out*/;
            resourceInputs["kubeConfigId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["kubeConfig"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(SkeKubeconfig.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SkeKubeconfig resources.
 */
export interface SkeKubeconfigState {
    /**
     * Name of the SKE cluster.
     */
    clusterName?: pulumi.Input<string>;
    /**
     * Date-time when the kubeconfig was created
     */
    creationTime?: pulumi.Input<string>;
    /**
     * Expiration time of the kubeconfig, in seconds. Defaults to `3600`
     */
    expiration?: pulumi.Input<number>;
    /**
     * Timestamp when the kubeconfig expires
     */
    expiresAt?: pulumi.Input<string>;
    /**
     * Raw short-lived admin kubeconfig.
     */
    kubeConfig?: pulumi.Input<string>;
    kubeConfigId?: pulumi.Input<string>;
    /**
     * STACKIT project ID to which the cluster is associated.
     */
    projectId?: pulumi.Input<string>;
    /**
     * If set to true, the provider will check if the kubeconfig has expired and will generated a new valid one in-place
     */
    refresh?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a SkeKubeconfig resource.
 */
export interface SkeKubeconfigArgs {
    /**
     * Name of the SKE cluster.
     */
    clusterName: pulumi.Input<string>;
    /**
     * Expiration time of the kubeconfig, in seconds. Defaults to `3600`
     */
    expiration?: pulumi.Input<number>;
    /**
     * STACKIT project ID to which the cluster is associated.
     */
    projectId: pulumi.Input<string>;
    /**
     * If set to true, the provider will check if the kubeconfig has expired and will generated a new valid one in-place
     */
    refresh?: pulumi.Input<boolean>;
}
