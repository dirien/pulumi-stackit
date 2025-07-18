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

    public sealed class MongodbflexInstanceOptionsGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The number of days that daily backups will be retained.
        /// </summary>
        [Input("dailySnapshotRetentionDays")]
        public Input<int>? DailySnapshotRetentionDays { get; set; }

        /// <summary>
        /// The number of months that monthly backups will be retained.
        /// </summary>
        [Input("monthlySnapshotRetentionMonths")]
        public Input<int>? MonthlySnapshotRetentionMonths { get; set; }

        /// <summary>
        /// The number of hours back in time the point-in-time recovery feature will be able to recover.
        /// </summary>
        [Input("pointInTimeWindowHours", required: true)]
        public Input<int> PointInTimeWindowHours { get; set; } = null!;

        /// <summary>
        /// The number of days that continuous backups (controlled via the `backup_schedule`) will be retained.
        /// </summary>
        [Input("snapshotRetentionDays")]
        public Input<int>? SnapshotRetentionDays { get; set; }

        /// <summary>
        /// Type of the MongoDB Flex instance. Supported values are: `Replica`, `Sharded`, `Single`.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        /// <summary>
        /// The number of weeks that weekly backups will be retained.
        /// </summary>
        [Input("weeklySnapshotRetentionWeeks")]
        public Input<int>? WeeklySnapshotRetentionWeeks { get; set; }

        public MongodbflexInstanceOptionsGetArgs()
        {
        }
        public static new MongodbflexInstanceOptionsGetArgs Empty => new MongodbflexInstanceOptionsGetArgs();
    }
}
