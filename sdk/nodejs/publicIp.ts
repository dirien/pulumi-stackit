// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Public IP resource schema. Must have a `region` specified in the provider configuration.
 *
 * ## Example Usage
 */
export class PublicIp extends pulumi.CustomResource {
    /**
     * Get an existing PublicIp resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PublicIpState, opts?: pulumi.CustomResourceOptions): PublicIp {
        return new PublicIp(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'stackit:index/publicIp:PublicIp';

    /**
     * Returns true if the given object is an instance of PublicIp.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PublicIp {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PublicIp.__pulumiType;
    }

    /**
     * The IP address.
     */
    public /*out*/ readonly ip!: pulumi.Output<string>;
    /**
     * Labels are key-value string pairs which can be attached to a resource container
     */
    public readonly labels!: pulumi.Output<{[key: string]: string} | undefined>;
    public readonly networkInterfaceId!: pulumi.Output<string>;
    /**
     * STACKIT project ID to which the public IP is associated.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * The public IP ID.
     */
    public /*out*/ readonly publicIpId!: pulumi.Output<string>;

    /**
     * Create a PublicIp resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PublicIpArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PublicIpArgs | PublicIpState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PublicIpState | undefined;
            resourceInputs["ip"] = state ? state.ip : undefined;
            resourceInputs["labels"] = state ? state.labels : undefined;
            resourceInputs["networkInterfaceId"] = state ? state.networkInterfaceId : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["publicIpId"] = state ? state.publicIpId : undefined;
        } else {
            const args = argsOrState as PublicIpArgs | undefined;
            if ((!args || args.projectId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectId'");
            }
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["networkInterfaceId"] = args ? args.networkInterfaceId : undefined;
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["ip"] = undefined /*out*/;
            resourceInputs["publicIpId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(PublicIp.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PublicIp resources.
 */
export interface PublicIpState {
    /**
     * The IP address.
     */
    ip?: pulumi.Input<string>;
    /**
     * Labels are key-value string pairs which can be attached to a resource container
     */
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    networkInterfaceId?: pulumi.Input<string>;
    /**
     * STACKIT project ID to which the public IP is associated.
     */
    projectId?: pulumi.Input<string>;
    /**
     * The public IP ID.
     */
    publicIpId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PublicIp resource.
 */
export interface PublicIpArgs {
    /**
     * Labels are key-value string pairs which can be attached to a resource container
     */
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    networkInterfaceId?: pulumi.Input<string>;
    /**
     * STACKIT project ID to which the public IP is associated.
     */
    projectId: pulumi.Input<string>;
}
