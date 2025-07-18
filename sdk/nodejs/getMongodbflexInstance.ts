// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * MongoDB Flex instance data source schema. Must have a `region` specified in the provider configuration.
 *
 * ## Example Usage
 */
export function getMongodbflexInstance(args: GetMongodbflexInstanceArgs, opts?: pulumi.InvokeOptions): Promise<GetMongodbflexInstanceResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("stackit:index/getMongodbflexInstance:getMongodbflexInstance", {
        "instanceId": args.instanceId,
        "projectId": args.projectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getMongodbflexInstance.
 */
export interface GetMongodbflexInstanceArgs {
    /**
     * ID of the MongoDB Flex instance.
     */
    instanceId: string;
    /**
     * STACKIT project ID to which the instance is associated.
     */
    projectId: string;
}

/**
 * A collection of values returned by getMongodbflexInstance.
 */
export interface GetMongodbflexInstanceResult {
    /**
     * The Access Control List (ACL) for the MongoDB Flex instance.
     */
    readonly acls: string[];
    /**
     * The backup schedule. Should follow the cron scheduling system format (e.g. "0 0 * * *").
     */
    readonly backupSchedule: string;
    readonly flavor: outputs.GetMongodbflexInstanceFlavor;
    readonly id: string;
    /**
     * ID of the MongoDB Flex instance.
     */
    readonly instanceId: string;
    /**
     * Instance name.
     */
    readonly name: string;
    /**
     * Custom parameters for the MongoDB Flex instance.
     */
    readonly options: outputs.GetMongodbflexInstanceOptions;
    /**
     * STACKIT project ID to which the instance is associated.
     */
    readonly projectId: string;
    readonly replicas: number;
    readonly storage: outputs.GetMongodbflexInstanceStorage;
    readonly version: string;
}
/**
 * MongoDB Flex instance data source schema. Must have a `region` specified in the provider configuration.
 *
 * ## Example Usage
 */
export function getMongodbflexInstanceOutput(args: GetMongodbflexInstanceOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetMongodbflexInstanceResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("stackit:index/getMongodbflexInstance:getMongodbflexInstance", {
        "instanceId": args.instanceId,
        "projectId": args.projectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getMongodbflexInstance.
 */
export interface GetMongodbflexInstanceOutputArgs {
    /**
     * ID of the MongoDB Flex instance.
     */
    instanceId: pulumi.Input<string>;
    /**
     * STACKIT project ID to which the instance is associated.
     */
    projectId: pulumi.Input<string>;
}
