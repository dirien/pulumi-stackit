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

    public sealed class SqlserverflexInstanceStorageGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("class")]
        public Input<string>? Class { get; set; }

        [Input("size")]
        public Input<int>? Size { get; set; }

        public SqlserverflexInstanceStorageGetArgs()
        {
        }
        public static new SqlserverflexInstanceStorageGetArgs Empty => new SqlserverflexInstanceStorageGetArgs();
    }
}
