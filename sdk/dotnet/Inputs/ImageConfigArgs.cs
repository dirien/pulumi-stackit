// *** WARNING: this file was generated by pulumi-language-dotnet. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace ediri.Stackit.Inputs
{

    public sealed class ImageConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Enables the BIOS bootmenu.
        /// </summary>
        [Input("bootMenu")]
        public Input<bool>? BootMenu { get; set; }

        /// <summary>
        /// Sets CDROM bus controller type.
        /// </summary>
        [Input("cdromBus")]
        public Input<string>? CdromBus { get; set; }

        /// <summary>
        /// Sets Disk bus controller type.
        /// </summary>
        [Input("diskBus")]
        public Input<string>? DiskBus { get; set; }

        /// <summary>
        /// Sets virtual network interface model.
        /// </summary>
        [Input("nicModel")]
        public Input<string>? NicModel { get; set; }

        /// <summary>
        /// Enables operating system specific optimizations.
        /// </summary>
        [Input("operatingSystem")]
        public Input<string>? OperatingSystem { get; set; }

        /// <summary>
        /// Operating system distribution.
        /// </summary>
        [Input("operatingSystemDistro")]
        public Input<string>? OperatingSystemDistro { get; set; }

        /// <summary>
        /// Version of the operating system.
        /// </summary>
        [Input("operatingSystemVersion")]
        public Input<string>? OperatingSystemVersion { get; set; }

        /// <summary>
        /// Sets the device bus when the image is used as a rescue image.
        /// </summary>
        [Input("rescueBus")]
        public Input<string>? RescueBus { get; set; }

        /// <summary>
        /// Sets the device when the image is used as a rescue image.
        /// </summary>
        [Input("rescueDevice")]
        public Input<string>? RescueDevice { get; set; }

        /// <summary>
        /// Enables Secure Boot.
        /// </summary>
        [Input("secureBoot")]
        public Input<bool>? SecureBoot { get; set; }

        /// <summary>
        /// Enables UEFI boot.
        /// </summary>
        [Input("uefi")]
        public Input<bool>? Uefi { get; set; }

        /// <summary>
        /// Sets Graphic device model.
        /// </summary>
        [Input("videoModel")]
        public Input<string>? VideoModel { get; set; }

        /// <summary>
        /// Enables the use of VirtIO SCSI to provide block device access. By default instances use VirtIO Block.
        /// </summary>
        [Input("virtioScsi")]
        public Input<bool>? VirtioScsi { get; set; }

        public ImageConfigArgs()
        {
        }
        public static new ImageConfigArgs Empty => new ImageConfigArgs();
    }
}
