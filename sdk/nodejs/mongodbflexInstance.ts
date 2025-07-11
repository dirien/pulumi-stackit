// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * MongoDB Flex instance resource schema. Must have a `region` specified in the provider configuration.
 *
 * ## Example Usage
 */
export class MongodbflexInstance extends pulumi.CustomResource {
    /**
     * Get an existing MongodbflexInstance resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MongodbflexInstanceState, opts?: pulumi.CustomResourceOptions): MongodbflexInstance {
        return new MongodbflexInstance(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'stackit:index/mongodbflexInstance:MongodbflexInstance';

    /**
     * Returns true if the given object is an instance of MongodbflexInstance.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MongodbflexInstance {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MongodbflexInstance.__pulumiType;
    }

    /**
     * The Access Control List (ACL) for the MongoDB Flex instance.
     */
    public readonly acls!: pulumi.Output<string[]>;
    /**
     * The backup schedule. Should follow the cron scheduling system format (e.g. "0 0 * * *").
     */
    public readonly backupSchedule!: pulumi.Output<string>;
    public readonly flavor!: pulumi.Output<outputs.MongodbflexInstanceFlavor>;
    /**
     * ID of the MongoDB Flex instance.
     */
    public /*out*/ readonly instanceId!: pulumi.Output<string>;
    /**
     * Instance name.
     */
    public readonly name!: pulumi.Output<string>;
    public readonly options!: pulumi.Output<outputs.MongodbflexInstanceOptions>;
    /**
     * STACKIT project ID to which the instance is associated.
     */
    public readonly projectId!: pulumi.Output<string>;
    public readonly replicas!: pulumi.Output<number>;
    public readonly storage!: pulumi.Output<outputs.MongodbflexInstanceStorage>;
    public readonly version!: pulumi.Output<string>;

    /**
     * Create a MongodbflexInstance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MongodbflexInstanceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MongodbflexInstanceArgs | MongodbflexInstanceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as MongodbflexInstanceState | undefined;
            resourceInputs["acls"] = state ? state.acls : undefined;
            resourceInputs["backupSchedule"] = state ? state.backupSchedule : undefined;
            resourceInputs["flavor"] = state ? state.flavor : undefined;
            resourceInputs["instanceId"] = state ? state.instanceId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["options"] = state ? state.options : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["replicas"] = state ? state.replicas : undefined;
            resourceInputs["storage"] = state ? state.storage : undefined;
            resourceInputs["version"] = state ? state.version : undefined;
        } else {
            const args = argsOrState as MongodbflexInstanceArgs | undefined;
            if ((!args || args.acls === undefined) && !opts.urn) {
                throw new Error("Missing required property 'acls'");
            }
            if ((!args || args.backupSchedule === undefined) && !opts.urn) {
                throw new Error("Missing required property 'backupSchedule'");
            }
            if ((!args || args.flavor === undefined) && !opts.urn) {
                throw new Error("Missing required property 'flavor'");
            }
            if ((!args || args.options === undefined) && !opts.urn) {
                throw new Error("Missing required property 'options'");
            }
            if ((!args || args.projectId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectId'");
            }
            if ((!args || args.replicas === undefined) && !opts.urn) {
                throw new Error("Missing required property 'replicas'");
            }
            if ((!args || args.storage === undefined) && !opts.urn) {
                throw new Error("Missing required property 'storage'");
            }
            if ((!args || args.version === undefined) && !opts.urn) {
                throw new Error("Missing required property 'version'");
            }
            resourceInputs["acls"] = args ? args.acls : undefined;
            resourceInputs["backupSchedule"] = args ? args.backupSchedule : undefined;
            resourceInputs["flavor"] = args ? args.flavor : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["options"] = args ? args.options : undefined;
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["replicas"] = args ? args.replicas : undefined;
            resourceInputs["storage"] = args ? args.storage : undefined;
            resourceInputs["version"] = args ? args.version : undefined;
            resourceInputs["instanceId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(MongodbflexInstance.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MongodbflexInstance resources.
 */
export interface MongodbflexInstanceState {
    /**
     * The Access Control List (ACL) for the MongoDB Flex instance.
     */
    acls?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The backup schedule. Should follow the cron scheduling system format (e.g. "0 0 * * *").
     */
    backupSchedule?: pulumi.Input<string>;
    flavor?: pulumi.Input<inputs.MongodbflexInstanceFlavor>;
    /**
     * ID of the MongoDB Flex instance.
     */
    instanceId?: pulumi.Input<string>;
    /**
     * Instance name.
     */
    name?: pulumi.Input<string>;
    options?: pulumi.Input<inputs.MongodbflexInstanceOptions>;
    /**
     * STACKIT project ID to which the instance is associated.
     */
    projectId?: pulumi.Input<string>;
    replicas?: pulumi.Input<number>;
    storage?: pulumi.Input<inputs.MongodbflexInstanceStorage>;
    version?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a MongodbflexInstance resource.
 */
export interface MongodbflexInstanceArgs {
    /**
     * The Access Control List (ACL) for the MongoDB Flex instance.
     */
    acls: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The backup schedule. Should follow the cron scheduling system format (e.g. "0 0 * * *").
     */
    backupSchedule: pulumi.Input<string>;
    flavor: pulumi.Input<inputs.MongodbflexInstanceFlavor>;
    /**
     * Instance name.
     */
    name?: pulumi.Input<string>;
    options: pulumi.Input<inputs.MongodbflexInstanceOptions>;
    /**
     * STACKIT project ID to which the instance is associated.
     */
    projectId: pulumi.Input<string>;
    replicas: pulumi.Input<number>;
    storage: pulumi.Input<inputs.MongodbflexInstanceStorage>;
    version: pulumi.Input<string>;
}
