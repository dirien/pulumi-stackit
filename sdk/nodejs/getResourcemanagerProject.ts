// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Resource Manager project data source schema. To identify the project, you need to provider either projectId or container_id. If you provide both, projectId will be used.
 *
 * ## Example Usage
 */
export function getResourcemanagerProject(args?: GetResourcemanagerProjectArgs, opts?: pulumi.InvokeOptions): Promise<GetResourcemanagerProjectResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("stackit:index/getResourcemanagerProject:getResourcemanagerProject", {
        "containerId": args.containerId,
        "projectId": args.projectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getResourcemanagerProject.
 */
export interface GetResourcemanagerProjectArgs {
    /**
     * Project container ID. Globally unique, user-friendly identifier.
     */
    containerId?: string;
    /**
     * Project UUID identifier. This is the ID that can be used in most of the other resources to identify the project.
     */
    projectId?: string;
}

/**
 * A collection of values returned by getResourcemanagerProject.
 */
export interface GetResourcemanagerProjectResult {
    /**
     * Project container ID. Globally unique, user-friendly identifier.
     */
    readonly containerId?: string;
    readonly id: string;
    /**
     * Labels are key-value string pairs which can be attached to a resource container. A label key must match the regex [A-ZÄÜÖa-zäüöß0-9*-]{1,64}. A label value must match the regex ^$|[A-ZÄÜÖa-zäüöß0-9*-]{1,64}
     */
    readonly labels: {[key: string]: string};
    /**
     * Project name.
     */
    readonly name: string;
    /**
     * Parent resource identifier. Both container ID (user-friendly) and UUID are supported
     */
    readonly parentContainerId: string;
    /**
     * Project UUID identifier. This is the ID that can be used in most of the other resources to identify the project.
     */
    readonly projectId?: string;
}
/**
 * Resource Manager project data source schema. To identify the project, you need to provider either projectId or container_id. If you provide both, projectId will be used.
 *
 * ## Example Usage
 */
export function getResourcemanagerProjectOutput(args?: GetResourcemanagerProjectOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetResourcemanagerProjectResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("stackit:index/getResourcemanagerProject:getResourcemanagerProject", {
        "containerId": args.containerId,
        "projectId": args.projectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getResourcemanagerProject.
 */
export interface GetResourcemanagerProjectOutputArgs {
    /**
     * Project container ID. Globally unique, user-friendly identifier.
     */
    containerId?: pulumi.Input<string>;
    /**
     * Project UUID identifier. This is the ID that can be used in most of the other resources to identify the project.
     */
    projectId?: pulumi.Input<string>;
}
