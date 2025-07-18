// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * MariaDB instance resource schema. Must have a `region` specified in the provider configuration.
 *
 * ## Example Usage
 */
export class MariadbInstance extends pulumi.CustomResource {
    /**
     * Get an existing MariadbInstance resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MariadbInstanceState, opts?: pulumi.CustomResourceOptions): MariadbInstance {
        return new MariadbInstance(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'stackit:index/mariadbInstance:MariadbInstance';

    /**
     * Returns true if the given object is an instance of MariadbInstance.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MariadbInstance {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MariadbInstance.__pulumiType;
    }

    public /*out*/ readonly cfGuid!: pulumi.Output<string>;
    public /*out*/ readonly cfOrganizationGuid!: pulumi.Output<string>;
    public /*out*/ readonly cfSpaceGuid!: pulumi.Output<string>;
    public /*out*/ readonly dashboardUrl!: pulumi.Output<string>;
    public /*out*/ readonly imageUrl!: pulumi.Output<string>;
    /**
     * ID of the MariaDB instance.
     */
    public /*out*/ readonly instanceId!: pulumi.Output<string>;
    /**
     * Instance name.
     */
    public readonly name!: pulumi.Output<string>;
    public readonly parameters!: pulumi.Output<outputs.MariadbInstanceParameters>;
    /**
     * The selected plan ID.
     */
    public /*out*/ readonly planId!: pulumi.Output<string>;
    /**
     * The selected plan name.
     */
    public readonly planName!: pulumi.Output<string>;
    /**
     * STACKIT project ID to which the instance is associated.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * The service version.
     */
    public readonly version!: pulumi.Output<string>;

    /**
     * Create a MariadbInstance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MariadbInstanceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MariadbInstanceArgs | MariadbInstanceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as MariadbInstanceState | undefined;
            resourceInputs["cfGuid"] = state ? state.cfGuid : undefined;
            resourceInputs["cfOrganizationGuid"] = state ? state.cfOrganizationGuid : undefined;
            resourceInputs["cfSpaceGuid"] = state ? state.cfSpaceGuid : undefined;
            resourceInputs["dashboardUrl"] = state ? state.dashboardUrl : undefined;
            resourceInputs["imageUrl"] = state ? state.imageUrl : undefined;
            resourceInputs["instanceId"] = state ? state.instanceId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["parameters"] = state ? state.parameters : undefined;
            resourceInputs["planId"] = state ? state.planId : undefined;
            resourceInputs["planName"] = state ? state.planName : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["version"] = state ? state.version : undefined;
        } else {
            const args = argsOrState as MariadbInstanceArgs | undefined;
            if ((!args || args.planName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'planName'");
            }
            if ((!args || args.projectId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectId'");
            }
            if ((!args || args.version === undefined) && !opts.urn) {
                throw new Error("Missing required property 'version'");
            }
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["parameters"] = args ? args.parameters : undefined;
            resourceInputs["planName"] = args ? args.planName : undefined;
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["version"] = args ? args.version : undefined;
            resourceInputs["cfGuid"] = undefined /*out*/;
            resourceInputs["cfOrganizationGuid"] = undefined /*out*/;
            resourceInputs["cfSpaceGuid"] = undefined /*out*/;
            resourceInputs["dashboardUrl"] = undefined /*out*/;
            resourceInputs["imageUrl"] = undefined /*out*/;
            resourceInputs["instanceId"] = undefined /*out*/;
            resourceInputs["planId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(MariadbInstance.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MariadbInstance resources.
 */
export interface MariadbInstanceState {
    cfGuid?: pulumi.Input<string>;
    cfOrganizationGuid?: pulumi.Input<string>;
    cfSpaceGuid?: pulumi.Input<string>;
    dashboardUrl?: pulumi.Input<string>;
    imageUrl?: pulumi.Input<string>;
    /**
     * ID of the MariaDB instance.
     */
    instanceId?: pulumi.Input<string>;
    /**
     * Instance name.
     */
    name?: pulumi.Input<string>;
    parameters?: pulumi.Input<inputs.MariadbInstanceParameters>;
    /**
     * The selected plan ID.
     */
    planId?: pulumi.Input<string>;
    /**
     * The selected plan name.
     */
    planName?: pulumi.Input<string>;
    /**
     * STACKIT project ID to which the instance is associated.
     */
    projectId?: pulumi.Input<string>;
    /**
     * The service version.
     */
    version?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a MariadbInstance resource.
 */
export interface MariadbInstanceArgs {
    /**
     * Instance name.
     */
    name?: pulumi.Input<string>;
    parameters?: pulumi.Input<inputs.MariadbInstanceParameters>;
    /**
     * The selected plan name.
     */
    planName: pulumi.Input<string>;
    /**
     * STACKIT project ID to which the instance is associated.
     */
    projectId: pulumi.Input<string>;
    /**
     * The service version.
     */
    version: pulumi.Input<string>;
}
