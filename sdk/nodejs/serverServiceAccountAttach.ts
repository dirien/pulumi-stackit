// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Service account attachment resource schema. Attaches a service account to a server. Must have a `region` specified in the provider configuration.
 *
 * ## Example Usage
 */
export class ServerServiceAccountAttach extends pulumi.CustomResource {
    /**
     * Get an existing ServerServiceAccountAttach resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServerServiceAccountAttachState, opts?: pulumi.CustomResourceOptions): ServerServiceAccountAttach {
        return new ServerServiceAccountAttach(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'stackit:index/serverServiceAccountAttach:ServerServiceAccountAttach';

    /**
     * Returns true if the given object is an instance of ServerServiceAccountAttach.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ServerServiceAccountAttach {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ServerServiceAccountAttach.__pulumiType;
    }

    /**
     * STACKIT project ID to which the service account attachment is associated.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * The server ID.
     */
    public readonly serverId!: pulumi.Output<string>;
    /**
     * The service account email.
     */
    public readonly serviceAccountEmail!: pulumi.Output<string>;

    /**
     * Create a ServerServiceAccountAttach resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ServerServiceAccountAttachArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ServerServiceAccountAttachArgs | ServerServiceAccountAttachState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ServerServiceAccountAttachState | undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["serverId"] = state ? state.serverId : undefined;
            resourceInputs["serviceAccountEmail"] = state ? state.serviceAccountEmail : undefined;
        } else {
            const args = argsOrState as ServerServiceAccountAttachArgs | undefined;
            if ((!args || args.projectId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectId'");
            }
            if ((!args || args.serverId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serverId'");
            }
            if ((!args || args.serviceAccountEmail === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceAccountEmail'");
            }
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["serverId"] = args ? args.serverId : undefined;
            resourceInputs["serviceAccountEmail"] = args ? args.serviceAccountEmail : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ServerServiceAccountAttach.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ServerServiceAccountAttach resources.
 */
export interface ServerServiceAccountAttachState {
    /**
     * STACKIT project ID to which the service account attachment is associated.
     */
    projectId?: pulumi.Input<string>;
    /**
     * The server ID.
     */
    serverId?: pulumi.Input<string>;
    /**
     * The service account email.
     */
    serviceAccountEmail?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ServerServiceAccountAttach resource.
 */
export interface ServerServiceAccountAttachArgs {
    /**
     * STACKIT project ID to which the service account attachment is associated.
     */
    projectId: pulumi.Input<string>;
    /**
     * The server ID.
     */
    serverId: pulumi.Input<string>;
    /**
     * The service account email.
     */
    serviceAccountEmail: pulumi.Input<string>;
}
