// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Postgres Flex database resource schema. Must have a `region` specified in the provider configuration.
 *
 * ## Example Usage
 */
export class PostgresflexDatabase extends pulumi.CustomResource {
    /**
     * Get an existing PostgresflexDatabase resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PostgresflexDatabaseState, opts?: pulumi.CustomResourceOptions): PostgresflexDatabase {
        return new PostgresflexDatabase(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'stackit:index/postgresflexDatabase:PostgresflexDatabase';

    /**
     * Returns true if the given object is an instance of PostgresflexDatabase.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PostgresflexDatabase {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PostgresflexDatabase.__pulumiType;
    }

    /**
     * Database ID.
     */
    public /*out*/ readonly databaseId!: pulumi.Output<string>;
    /**
     * ID of the Postgres Flex instance.
     */
    public readonly instanceId!: pulumi.Output<string>;
    /**
     * Database name.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Username of the database owner.
     */
    public readonly owner!: pulumi.Output<string>;
    /**
     * STACKIT project ID to which the instance is associated.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * The resource region. If not defined, the provider region is used.
     */
    public readonly region!: pulumi.Output<string>;

    /**
     * Create a PostgresflexDatabase resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PostgresflexDatabaseArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PostgresflexDatabaseArgs | PostgresflexDatabaseState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PostgresflexDatabaseState | undefined;
            resourceInputs["databaseId"] = state ? state.databaseId : undefined;
            resourceInputs["instanceId"] = state ? state.instanceId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["owner"] = state ? state.owner : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
        } else {
            const args = argsOrState as PostgresflexDatabaseArgs | undefined;
            if ((!args || args.instanceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceId'");
            }
            if ((!args || args.owner === undefined) && !opts.urn) {
                throw new Error("Missing required property 'owner'");
            }
            if ((!args || args.projectId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'projectId'");
            }
            resourceInputs["instanceId"] = args ? args.instanceId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["owner"] = args ? args.owner : undefined;
            resourceInputs["projectId"] = args ? args.projectId : undefined;
            resourceInputs["region"] = args ? args.region : undefined;
            resourceInputs["databaseId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(PostgresflexDatabase.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PostgresflexDatabase resources.
 */
export interface PostgresflexDatabaseState {
    /**
     * Database ID.
     */
    databaseId?: pulumi.Input<string>;
    /**
     * ID of the Postgres Flex instance.
     */
    instanceId?: pulumi.Input<string>;
    /**
     * Database name.
     */
    name?: pulumi.Input<string>;
    /**
     * Username of the database owner.
     */
    owner?: pulumi.Input<string>;
    /**
     * STACKIT project ID to which the instance is associated.
     */
    projectId?: pulumi.Input<string>;
    /**
     * The resource region. If not defined, the provider region is used.
     */
    region?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PostgresflexDatabase resource.
 */
export interface PostgresflexDatabaseArgs {
    /**
     * ID of the Postgres Flex instance.
     */
    instanceId: pulumi.Input<string>;
    /**
     * Database name.
     */
    name?: pulumi.Input<string>;
    /**
     * Username of the database owner.
     */
    owner: pulumi.Input<string>;
    /**
     * STACKIT project ID to which the instance is associated.
     */
    projectId: pulumi.Input<string>;
    /**
     * The resource region. If not defined, the provider region is used.
     */
    region?: pulumi.Input<string>;
}
