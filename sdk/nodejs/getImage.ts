// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Image datasource schema. Must have a `region` specified in the provider configuration.
 *
 * ## Example Usage
 */
export function getImage(args: GetImageArgs, opts?: pulumi.InvokeOptions): Promise<GetImageResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("stackit:index/getImage:getImage", {
        "imageId": args.imageId,
        "projectId": args.projectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getImage.
 */
export interface GetImageArgs {
    /**
     * The image ID.
     */
    imageId: string;
    /**
     * STACKIT project ID to which the image is associated.
     */
    projectId: string;
}

/**
 * A collection of values returned by getImage.
 */
export interface GetImageResult {
    /**
     * Representation of an image checksum.
     */
    readonly checksum: outputs.GetImageChecksum;
    /**
     * Properties to set hardware and scheduling settings for an image.
     */
    readonly config: outputs.GetImageConfig;
    /**
     * The disk format of the image.
     */
    readonly diskFormat: string;
    readonly id: string;
    /**
     * The image ID.
     */
    readonly imageId: string;
    /**
     * Labels are key-value string pairs which can be attached to a resource container
     */
    readonly labels: {[key: string]: string};
    /**
     * The minimum disk size of the image in GB.
     */
    readonly minDiskSize: number;
    /**
     * The minimum RAM of the image in MB.
     */
    readonly minRam: number;
    /**
     * The name of the image.
     */
    readonly name: string;
    /**
     * STACKIT project ID to which the image is associated.
     */
    readonly projectId: string;
    /**
     * Whether the image is protected.
     */
    readonly protected: boolean;
    /**
     * The scope of the image.
     */
    readonly scope: string;
}
/**
 * Image datasource schema. Must have a `region` specified in the provider configuration.
 *
 * ## Example Usage
 */
export function getImageOutput(args: GetImageOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetImageResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("stackit:index/getImage:getImage", {
        "imageId": args.imageId,
        "projectId": args.projectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getImage.
 */
export interface GetImageOutputArgs {
    /**
     * The image ID.
     */
    imageId: pulumi.Input<string>;
    /**
     * STACKIT project ID to which the image is associated.
     */
    projectId: pulumi.Input<string>;
}
