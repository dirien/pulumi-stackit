// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package stackit

import (
	"context"
	"reflect"

	"errors"
	"github.com/dirien/pulumi-stackit/sdk/go/stackit/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Server backup schedule resource schema. Must have a `region` specified in the provider configuration.
//
// > This resource is in beta and may be subject to breaking changes in the future. Use with caution. See our guide for how to opt-in to use beta resources.
//
// ## Example Usage
type ServerBackupSchedule struct {
	pulumi.CustomResourceState

	// Backup schedule details for the backups.
	BackupProperties ServerBackupScheduleBackupPropertiesOutput `pulumi:"backupProperties"`
	// Backup schedule ID.
	BackupScheduleId pulumi.IntOutput `pulumi:"backupScheduleId"`
	// Is the backup schedule enabled or disabled.
	Enabled pulumi.BoolOutput `pulumi:"enabled"`
	// The schedule name.
	Name pulumi.StringOutput `pulumi:"name"`
	// STACKIT Project ID to which the server is associated.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// The resource region. If not defined, the provider region is used.
	Region pulumi.StringOutput `pulumi:"region"`
	// Backup schedule described in `rrule` (recurrence rule) format.
	Rrule pulumi.StringOutput `pulumi:"rrule"`
	// Server ID for the backup schedule.
	ServerId pulumi.StringOutput `pulumi:"serverId"`
}

// NewServerBackupSchedule registers a new resource with the given unique name, arguments, and options.
func NewServerBackupSchedule(ctx *pulumi.Context,
	name string, args *ServerBackupScheduleArgs, opts ...pulumi.ResourceOption) (*ServerBackupSchedule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.BackupProperties == nil {
		return nil, errors.New("invalid value for required argument 'BackupProperties'")
	}
	if args.Enabled == nil {
		return nil, errors.New("invalid value for required argument 'Enabled'")
	}
	if args.ProjectId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectId'")
	}
	if args.Rrule == nil {
		return nil, errors.New("invalid value for required argument 'Rrule'")
	}
	if args.ServerId == nil {
		return nil, errors.New("invalid value for required argument 'ServerId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ServerBackupSchedule
	err := ctx.RegisterResource("stackit:index/serverBackupSchedule:ServerBackupSchedule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServerBackupSchedule gets an existing ServerBackupSchedule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServerBackupSchedule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServerBackupScheduleState, opts ...pulumi.ResourceOption) (*ServerBackupSchedule, error) {
	var resource ServerBackupSchedule
	err := ctx.ReadResource("stackit:index/serverBackupSchedule:ServerBackupSchedule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ServerBackupSchedule resources.
type serverBackupScheduleState struct {
	// Backup schedule details for the backups.
	BackupProperties *ServerBackupScheduleBackupProperties `pulumi:"backupProperties"`
	// Backup schedule ID.
	BackupScheduleId *int `pulumi:"backupScheduleId"`
	// Is the backup schedule enabled or disabled.
	Enabled *bool `pulumi:"enabled"`
	// The schedule name.
	Name *string `pulumi:"name"`
	// STACKIT Project ID to which the server is associated.
	ProjectId *string `pulumi:"projectId"`
	// The resource region. If not defined, the provider region is used.
	Region *string `pulumi:"region"`
	// Backup schedule described in `rrule` (recurrence rule) format.
	Rrule *string `pulumi:"rrule"`
	// Server ID for the backup schedule.
	ServerId *string `pulumi:"serverId"`
}

type ServerBackupScheduleState struct {
	// Backup schedule details for the backups.
	BackupProperties ServerBackupScheduleBackupPropertiesPtrInput
	// Backup schedule ID.
	BackupScheduleId pulumi.IntPtrInput
	// Is the backup schedule enabled or disabled.
	Enabled pulumi.BoolPtrInput
	// The schedule name.
	Name pulumi.StringPtrInput
	// STACKIT Project ID to which the server is associated.
	ProjectId pulumi.StringPtrInput
	// The resource region. If not defined, the provider region is used.
	Region pulumi.StringPtrInput
	// Backup schedule described in `rrule` (recurrence rule) format.
	Rrule pulumi.StringPtrInput
	// Server ID for the backup schedule.
	ServerId pulumi.StringPtrInput
}

func (ServerBackupScheduleState) ElementType() reflect.Type {
	return reflect.TypeOf((*serverBackupScheduleState)(nil)).Elem()
}

type serverBackupScheduleArgs struct {
	// Backup schedule details for the backups.
	BackupProperties ServerBackupScheduleBackupProperties `pulumi:"backupProperties"`
	// Is the backup schedule enabled or disabled.
	Enabled bool `pulumi:"enabled"`
	// The schedule name.
	Name *string `pulumi:"name"`
	// STACKIT Project ID to which the server is associated.
	ProjectId string `pulumi:"projectId"`
	// The resource region. If not defined, the provider region is used.
	Region *string `pulumi:"region"`
	// Backup schedule described in `rrule` (recurrence rule) format.
	Rrule string `pulumi:"rrule"`
	// Server ID for the backup schedule.
	ServerId string `pulumi:"serverId"`
}

// The set of arguments for constructing a ServerBackupSchedule resource.
type ServerBackupScheduleArgs struct {
	// Backup schedule details for the backups.
	BackupProperties ServerBackupScheduleBackupPropertiesInput
	// Is the backup schedule enabled or disabled.
	Enabled pulumi.BoolInput
	// The schedule name.
	Name pulumi.StringPtrInput
	// STACKIT Project ID to which the server is associated.
	ProjectId pulumi.StringInput
	// The resource region. If not defined, the provider region is used.
	Region pulumi.StringPtrInput
	// Backup schedule described in `rrule` (recurrence rule) format.
	Rrule pulumi.StringInput
	// Server ID for the backup schedule.
	ServerId pulumi.StringInput
}

func (ServerBackupScheduleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serverBackupScheduleArgs)(nil)).Elem()
}

type ServerBackupScheduleInput interface {
	pulumi.Input

	ToServerBackupScheduleOutput() ServerBackupScheduleOutput
	ToServerBackupScheduleOutputWithContext(ctx context.Context) ServerBackupScheduleOutput
}

func (*ServerBackupSchedule) ElementType() reflect.Type {
	return reflect.TypeOf((**ServerBackupSchedule)(nil)).Elem()
}

func (i *ServerBackupSchedule) ToServerBackupScheduleOutput() ServerBackupScheduleOutput {
	return i.ToServerBackupScheduleOutputWithContext(context.Background())
}

func (i *ServerBackupSchedule) ToServerBackupScheduleOutputWithContext(ctx context.Context) ServerBackupScheduleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServerBackupScheduleOutput)
}

// ServerBackupScheduleArrayInput is an input type that accepts ServerBackupScheduleArray and ServerBackupScheduleArrayOutput values.
// You can construct a concrete instance of `ServerBackupScheduleArrayInput` via:
//
//	ServerBackupScheduleArray{ ServerBackupScheduleArgs{...} }
type ServerBackupScheduleArrayInput interface {
	pulumi.Input

	ToServerBackupScheduleArrayOutput() ServerBackupScheduleArrayOutput
	ToServerBackupScheduleArrayOutputWithContext(context.Context) ServerBackupScheduleArrayOutput
}

type ServerBackupScheduleArray []ServerBackupScheduleInput

func (ServerBackupScheduleArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ServerBackupSchedule)(nil)).Elem()
}

func (i ServerBackupScheduleArray) ToServerBackupScheduleArrayOutput() ServerBackupScheduleArrayOutput {
	return i.ToServerBackupScheduleArrayOutputWithContext(context.Background())
}

func (i ServerBackupScheduleArray) ToServerBackupScheduleArrayOutputWithContext(ctx context.Context) ServerBackupScheduleArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServerBackupScheduleArrayOutput)
}

// ServerBackupScheduleMapInput is an input type that accepts ServerBackupScheduleMap and ServerBackupScheduleMapOutput values.
// You can construct a concrete instance of `ServerBackupScheduleMapInput` via:
//
//	ServerBackupScheduleMap{ "key": ServerBackupScheduleArgs{...} }
type ServerBackupScheduleMapInput interface {
	pulumi.Input

	ToServerBackupScheduleMapOutput() ServerBackupScheduleMapOutput
	ToServerBackupScheduleMapOutputWithContext(context.Context) ServerBackupScheduleMapOutput
}

type ServerBackupScheduleMap map[string]ServerBackupScheduleInput

func (ServerBackupScheduleMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ServerBackupSchedule)(nil)).Elem()
}

func (i ServerBackupScheduleMap) ToServerBackupScheduleMapOutput() ServerBackupScheduleMapOutput {
	return i.ToServerBackupScheduleMapOutputWithContext(context.Background())
}

func (i ServerBackupScheduleMap) ToServerBackupScheduleMapOutputWithContext(ctx context.Context) ServerBackupScheduleMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServerBackupScheduleMapOutput)
}

type ServerBackupScheduleOutput struct{ *pulumi.OutputState }

func (ServerBackupScheduleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ServerBackupSchedule)(nil)).Elem()
}

func (o ServerBackupScheduleOutput) ToServerBackupScheduleOutput() ServerBackupScheduleOutput {
	return o
}

func (o ServerBackupScheduleOutput) ToServerBackupScheduleOutputWithContext(ctx context.Context) ServerBackupScheduleOutput {
	return o
}

// Backup schedule details for the backups.
func (o ServerBackupScheduleOutput) BackupProperties() ServerBackupScheduleBackupPropertiesOutput {
	return o.ApplyT(func(v *ServerBackupSchedule) ServerBackupScheduleBackupPropertiesOutput { return v.BackupProperties }).(ServerBackupScheduleBackupPropertiesOutput)
}

// Backup schedule ID.
func (o ServerBackupScheduleOutput) BackupScheduleId() pulumi.IntOutput {
	return o.ApplyT(func(v *ServerBackupSchedule) pulumi.IntOutput { return v.BackupScheduleId }).(pulumi.IntOutput)
}

// Is the backup schedule enabled or disabled.
func (o ServerBackupScheduleOutput) Enabled() pulumi.BoolOutput {
	return o.ApplyT(func(v *ServerBackupSchedule) pulumi.BoolOutput { return v.Enabled }).(pulumi.BoolOutput)
}

// The schedule name.
func (o ServerBackupScheduleOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ServerBackupSchedule) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// STACKIT Project ID to which the server is associated.
func (o ServerBackupScheduleOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v *ServerBackupSchedule) pulumi.StringOutput { return v.ProjectId }).(pulumi.StringOutput)
}

// The resource region. If not defined, the provider region is used.
func (o ServerBackupScheduleOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v *ServerBackupSchedule) pulumi.StringOutput { return v.Region }).(pulumi.StringOutput)
}

// Backup schedule described in `rrule` (recurrence rule) format.
func (o ServerBackupScheduleOutput) Rrule() pulumi.StringOutput {
	return o.ApplyT(func(v *ServerBackupSchedule) pulumi.StringOutput { return v.Rrule }).(pulumi.StringOutput)
}

// Server ID for the backup schedule.
func (o ServerBackupScheduleOutput) ServerId() pulumi.StringOutput {
	return o.ApplyT(func(v *ServerBackupSchedule) pulumi.StringOutput { return v.ServerId }).(pulumi.StringOutput)
}

type ServerBackupScheduleArrayOutput struct{ *pulumi.OutputState }

func (ServerBackupScheduleArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ServerBackupSchedule)(nil)).Elem()
}

func (o ServerBackupScheduleArrayOutput) ToServerBackupScheduleArrayOutput() ServerBackupScheduleArrayOutput {
	return o
}

func (o ServerBackupScheduleArrayOutput) ToServerBackupScheduleArrayOutputWithContext(ctx context.Context) ServerBackupScheduleArrayOutput {
	return o
}

func (o ServerBackupScheduleArrayOutput) Index(i pulumi.IntInput) ServerBackupScheduleOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ServerBackupSchedule {
		return vs[0].([]*ServerBackupSchedule)[vs[1].(int)]
	}).(ServerBackupScheduleOutput)
}

type ServerBackupScheduleMapOutput struct{ *pulumi.OutputState }

func (ServerBackupScheduleMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ServerBackupSchedule)(nil)).Elem()
}

func (o ServerBackupScheduleMapOutput) ToServerBackupScheduleMapOutput() ServerBackupScheduleMapOutput {
	return o
}

func (o ServerBackupScheduleMapOutput) ToServerBackupScheduleMapOutputWithContext(ctx context.Context) ServerBackupScheduleMapOutput {
	return o
}

func (o ServerBackupScheduleMapOutput) MapIndex(k pulumi.StringInput) ServerBackupScheduleOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ServerBackupSchedule {
		return vs[0].(map[string]*ServerBackupSchedule)[vs[1].(string)]
	}).(ServerBackupScheduleOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ServerBackupScheduleInput)(nil)).Elem(), &ServerBackupSchedule{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServerBackupScheduleArrayInput)(nil)).Elem(), ServerBackupScheduleArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServerBackupScheduleMapInput)(nil)).Elem(), ServerBackupScheduleMap{})
	pulumi.RegisterOutputType(ServerBackupScheduleOutput{})
	pulumi.RegisterOutputType(ServerBackupScheduleArrayOutput{})
	pulumi.RegisterOutputType(ServerBackupScheduleMapOutput{})
}
