// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Service account key schema.
 * ## Example Usage
 *
 * ### Automatically rotate service account keys
 */
export class ServiceAccountKey extends pulumi.CustomResource {
    /**
     * Get an existing ServiceAccountKey resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServiceAccountKeyState, opts?: pulumi.CustomResourceOptions): ServiceAccountKey {
        return new ServiceAccountKey(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'stackit:index/serviceAccountKey:ServiceAccountKey';

    /**
     * Returns true if the given object is an instance of ServiceAccountKey.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ServiceAccountKey {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ServiceAccountKey.__pulumiType;
    }

    /**
     * The raw JSON representation of the service account key json, available for direct use.
     */
    public /*out*/ readonly json!: pulumi.Output<string>;
    /**
     * The unique identifier for the key associated with the service account.
     */
    public /*out*/ readonly keyId!: pulumi.Output<string>;
    /**
     * The STACKIT project ID associated with the service account key.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * Specifies the public*key (RSA2048 key-pair). If not provided, a certificate from STACKIT will be used to generate a private*key.
     */
    public readonly publicKey!: pulumi.Output<string | undefined>;
    /**
     * A map of arbitrary key/value pairs designed to force key recreation when they change, facilitating key rotation based on external factors such as a changing timestamp. Modifying this map triggers the creation of a new resource.
     */
    public readonly rotateWhenChanged!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The email address associated with the service account, used for account identification and communication.
     */
    public readonly serviceAccountEmail!: pulumi.Output<string>;
    /**
     * Specifies the key's validity duration in days. If left unspecified, the key is considered valid until it is deleted
     */
    public readonly ttlDays!: pulumi.Output<number | undefined>;

    /**
     * Create a ServiceAccountKey resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ServiceAccountKeyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ServiceAccountKeyArgs | ServiceAccountKeyState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ServiceAccountKeyState | undefined;
            resourceInputs["json"] = state ? state.json : undefined;
            resourceInputs["keyId"] = state ? state.keyId : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["publicKey"] = state ? state.publicKey : undefined;
            resourceInputs["rotateWhenChanged"] = state ? state.rotateWhenChanged : undefined;
            resourceInputs["serviceAccountEmail"] = state ? state.serviceAccountEmail : undefined;
            resourceInputs["ttlDays"] = state ? state.ttlDays : undefined;
        } else {
            const args = argsOrState as ServiceAccountKeyArgs | undefined;
            if ((!args || args.projectId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectId'");
            }
            if ((!args || args.serviceAccountEmail === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceAccountEmail'");
            }
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["publicKey"] = args ? args.publicKey : undefined;
            resourceInputs["rotateWhenChanged"] = args ? args.rotateWhenChanged : undefined;
            resourceInputs["serviceAccountEmail"] = args ? args.serviceAccountEmail : undefined;
            resourceInputs["ttlDays"] = args ? args.ttlDays : undefined;
            resourceInputs["json"] = undefined /*out*/;
            resourceInputs["keyId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["json"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(ServiceAccountKey.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ServiceAccountKey resources.
 */
export interface ServiceAccountKeyState {
    /**
     * The raw JSON representation of the service account key json, available for direct use.
     */
    json?: pulumi.Input<string>;
    /**
     * The unique identifier for the key associated with the service account.
     */
    keyId?: pulumi.Input<string>;
    /**
     * The STACKIT project ID associated with the service account key.
     */
    projectId?: pulumi.Input<string>;
    /**
     * Specifies the public*key (RSA2048 key-pair). If not provided, a certificate from STACKIT will be used to generate a private*key.
     */
    publicKey?: pulumi.Input<string>;
    /**
     * A map of arbitrary key/value pairs designed to force key recreation when they change, facilitating key rotation based on external factors such as a changing timestamp. Modifying this map triggers the creation of a new resource.
     */
    rotateWhenChanged?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The email address associated with the service account, used for account identification and communication.
     */
    serviceAccountEmail?: pulumi.Input<string>;
    /**
     * Specifies the key's validity duration in days. If left unspecified, the key is considered valid until it is deleted
     */
    ttlDays?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a ServiceAccountKey resource.
 */
export interface ServiceAccountKeyArgs {
    /**
     * The STACKIT project ID associated with the service account key.
     */
    projectId: pulumi.Input<string>;
    /**
     * Specifies the public*key (RSA2048 key-pair). If not provided, a certificate from STACKIT will be used to generate a private*key.
     */
    publicKey?: pulumi.Input<string>;
    /**
     * A map of arbitrary key/value pairs designed to force key recreation when they change, facilitating key rotation based on external factors such as a changing timestamp. Modifying this map triggers the creation of a new resource.
     */
    rotateWhenChanged?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The email address associated with the service account, used for account identification and communication.
     */
    serviceAccountEmail: pulumi.Input<string>;
    /**
     * Specifies the key's validity duration in days. If left unspecified, the key is considered valid until it is deleted
     */
    ttlDays?: pulumi.Input<number>;
}
