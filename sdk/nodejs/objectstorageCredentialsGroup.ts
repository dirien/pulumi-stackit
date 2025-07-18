// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ObjectStorage credentials group resource schema. Must have a `region` specified in the provider configuration. If you are creating `credentialsgroup` and `bucket` resources simultaneously, please include the `dependsOn` field so that they are created sequentially. This prevents errors from concurrent calls to the service enablement that is done in the background.
 *
 * ## Example Usage
 */
export class ObjectstorageCredentialsGroup extends pulumi.CustomResource {
    /**
     * Get an existing ObjectstorageCredentialsGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ObjectstorageCredentialsGroupState, opts?: pulumi.CustomResourceOptions): ObjectstorageCredentialsGroup {
        return new ObjectstorageCredentialsGroup(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'stackit:index/objectstorageCredentialsGroup:ObjectstorageCredentialsGroup';

    /**
     * Returns true if the given object is an instance of ObjectstorageCredentialsGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ObjectstorageCredentialsGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ObjectstorageCredentialsGroup.__pulumiType;
    }

    /**
     * The credentials group ID
     */
    public /*out*/ readonly credentialsGroupId!: pulumi.Output<string>;
    /**
     * The credentials group's display name.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Project ID to which the credentials group is associated.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * The resource region. If not defined, the provider region is used.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * Credentials group uniform resource name (URN)
     */
    public /*out*/ readonly urn!: pulumi.Output<string>;

    /**
     * Create a ObjectstorageCredentialsGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ObjectstorageCredentialsGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ObjectstorageCredentialsGroupArgs | ObjectstorageCredentialsGroupState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ObjectstorageCredentialsGroupState | undefined;
            resourceInputs["credentialsGroupId"] = state ? state.credentialsGroupId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["urn"] = state ? state.urn : undefined;
        } else {
            const args = argsOrState as ObjectstorageCredentialsGroupArgs | undefined;
            if ((!args || args.projectId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectId'");
            }
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["credentialsGroupId"] = undefined /*out*/;
            resourceInputs["urn"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ObjectstorageCredentialsGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ObjectstorageCredentialsGroup resources.
 */
export interface ObjectstorageCredentialsGroupState {
    /**
     * The credentials group ID
     */
    credentialsGroupId?: pulumi.Input<string>;
    /**
     * The credentials group's display name.
     */
    name?: pulumi.Input<string>;
    /**
     * Project ID to which the credentials group is associated.
     */
    projectId?: pulumi.Input<string>;
    /**
     * The resource region. If not defined, the provider region is used.
     */
    region?: pulumi.Input<string>;
    /**
     * Credentials group uniform resource name (URN)
     */
    urn?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ObjectstorageCredentialsGroup resource.
 */
export interface ObjectstorageCredentialsGroupArgs {
    /**
     * The credentials group's display name.
     */
    name?: pulumi.Input<string>;
    /**
     * Project ID to which the credentials group is associated.
     */
    projectId: pulumi.Input<string>;
    /**
     * The resource region. If not defined, the provider region is used.
     */
    region?: pulumi.Input<string>;
}
