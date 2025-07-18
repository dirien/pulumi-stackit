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

// LogMe credential resource schema. Must have a `region` specified in the provider configuration.
//
// ## Example Usage
type LogmeCredential struct {
	pulumi.CustomResourceState

	// The credential's ID.
	CredentialId pulumi.StringOutput `pulumi:"credentialId"`
	Host         pulumi.StringOutput `pulumi:"host"`
	// ID of the LogMe instance.
	InstanceId pulumi.StringOutput `pulumi:"instanceId"`
	Password   pulumi.StringOutput `pulumi:"password"`
	Port       pulumi.IntOutput    `pulumi:"port"`
	// STACKIT Project ID to which the instance is associated.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	Uri       pulumi.StringOutput `pulumi:"uri"`
	Username  pulumi.StringOutput `pulumi:"username"`
}

// NewLogmeCredential registers a new resource with the given unique name, arguments, and options.
func NewLogmeCredential(ctx *pulumi.Context,
	name string, args *LogmeCredentialArgs, opts ...pulumi.ResourceOption) (*LogmeCredential, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.InstanceId == nil {
		return nil, errors.New("invalid value for required argument 'InstanceId'")
	}
	if args.ProjectId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectId'")
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"password",
		"uri",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource LogmeCredential
	err := ctx.RegisterResource("stackit:index/logmeCredential:LogmeCredential", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLogmeCredential gets an existing LogmeCredential resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLogmeCredential(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LogmeCredentialState, opts ...pulumi.ResourceOption) (*LogmeCredential, error) {
	var resource LogmeCredential
	err := ctx.ReadResource("stackit:index/logmeCredential:LogmeCredential", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LogmeCredential resources.
type logmeCredentialState struct {
	// The credential's ID.
	CredentialId *string `pulumi:"credentialId"`
	Host         *string `pulumi:"host"`
	// ID of the LogMe instance.
	InstanceId *string `pulumi:"instanceId"`
	Password   *string `pulumi:"password"`
	Port       *int    `pulumi:"port"`
	// STACKIT Project ID to which the instance is associated.
	ProjectId *string `pulumi:"projectId"`
	Uri       *string `pulumi:"uri"`
	Username  *string `pulumi:"username"`
}

type LogmeCredentialState struct {
	// The credential's ID.
	CredentialId pulumi.StringPtrInput
	Host         pulumi.StringPtrInput
	// ID of the LogMe instance.
	InstanceId pulumi.StringPtrInput
	Password   pulumi.StringPtrInput
	Port       pulumi.IntPtrInput
	// STACKIT Project ID to which the instance is associated.
	ProjectId pulumi.StringPtrInput
	Uri       pulumi.StringPtrInput
	Username  pulumi.StringPtrInput
}

func (LogmeCredentialState) ElementType() reflect.Type {
	return reflect.TypeOf((*logmeCredentialState)(nil)).Elem()
}

type logmeCredentialArgs struct {
	// ID of the LogMe instance.
	InstanceId string `pulumi:"instanceId"`
	// STACKIT Project ID to which the instance is associated.
	ProjectId string `pulumi:"projectId"`
}

// The set of arguments for constructing a LogmeCredential resource.
type LogmeCredentialArgs struct {
	// ID of the LogMe instance.
	InstanceId pulumi.StringInput
	// STACKIT Project ID to which the instance is associated.
	ProjectId pulumi.StringInput
}

func (LogmeCredentialArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*logmeCredentialArgs)(nil)).Elem()
}

type LogmeCredentialInput interface {
	pulumi.Input

	ToLogmeCredentialOutput() LogmeCredentialOutput
	ToLogmeCredentialOutputWithContext(ctx context.Context) LogmeCredentialOutput
}

func (*LogmeCredential) ElementType() reflect.Type {
	return reflect.TypeOf((**LogmeCredential)(nil)).Elem()
}

func (i *LogmeCredential) ToLogmeCredentialOutput() LogmeCredentialOutput {
	return i.ToLogmeCredentialOutputWithContext(context.Background())
}

func (i *LogmeCredential) ToLogmeCredentialOutputWithContext(ctx context.Context) LogmeCredentialOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LogmeCredentialOutput)
}

// LogmeCredentialArrayInput is an input type that accepts LogmeCredentialArray and LogmeCredentialArrayOutput values.
// You can construct a concrete instance of `LogmeCredentialArrayInput` via:
//
//	LogmeCredentialArray{ LogmeCredentialArgs{...} }
type LogmeCredentialArrayInput interface {
	pulumi.Input

	ToLogmeCredentialArrayOutput() LogmeCredentialArrayOutput
	ToLogmeCredentialArrayOutputWithContext(context.Context) LogmeCredentialArrayOutput
}

type LogmeCredentialArray []LogmeCredentialInput

func (LogmeCredentialArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*LogmeCredential)(nil)).Elem()
}

func (i LogmeCredentialArray) ToLogmeCredentialArrayOutput() LogmeCredentialArrayOutput {
	return i.ToLogmeCredentialArrayOutputWithContext(context.Background())
}

func (i LogmeCredentialArray) ToLogmeCredentialArrayOutputWithContext(ctx context.Context) LogmeCredentialArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LogmeCredentialArrayOutput)
}

// LogmeCredentialMapInput is an input type that accepts LogmeCredentialMap and LogmeCredentialMapOutput values.
// You can construct a concrete instance of `LogmeCredentialMapInput` via:
//
//	LogmeCredentialMap{ "key": LogmeCredentialArgs{...} }
type LogmeCredentialMapInput interface {
	pulumi.Input

	ToLogmeCredentialMapOutput() LogmeCredentialMapOutput
	ToLogmeCredentialMapOutputWithContext(context.Context) LogmeCredentialMapOutput
}

type LogmeCredentialMap map[string]LogmeCredentialInput

func (LogmeCredentialMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*LogmeCredential)(nil)).Elem()
}

func (i LogmeCredentialMap) ToLogmeCredentialMapOutput() LogmeCredentialMapOutput {
	return i.ToLogmeCredentialMapOutputWithContext(context.Background())
}

func (i LogmeCredentialMap) ToLogmeCredentialMapOutputWithContext(ctx context.Context) LogmeCredentialMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LogmeCredentialMapOutput)
}

type LogmeCredentialOutput struct{ *pulumi.OutputState }

func (LogmeCredentialOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**LogmeCredential)(nil)).Elem()
}

func (o LogmeCredentialOutput) ToLogmeCredentialOutput() LogmeCredentialOutput {
	return o
}

func (o LogmeCredentialOutput) ToLogmeCredentialOutputWithContext(ctx context.Context) LogmeCredentialOutput {
	return o
}

// The credential's ID.
func (o LogmeCredentialOutput) CredentialId() pulumi.StringOutput {
	return o.ApplyT(func(v *LogmeCredential) pulumi.StringOutput { return v.CredentialId }).(pulumi.StringOutput)
}

func (o LogmeCredentialOutput) Host() pulumi.StringOutput {
	return o.ApplyT(func(v *LogmeCredential) pulumi.StringOutput { return v.Host }).(pulumi.StringOutput)
}

// ID of the LogMe instance.
func (o LogmeCredentialOutput) InstanceId() pulumi.StringOutput {
	return o.ApplyT(func(v *LogmeCredential) pulumi.StringOutput { return v.InstanceId }).(pulumi.StringOutput)
}

func (o LogmeCredentialOutput) Password() pulumi.StringOutput {
	return o.ApplyT(func(v *LogmeCredential) pulumi.StringOutput { return v.Password }).(pulumi.StringOutput)
}

func (o LogmeCredentialOutput) Port() pulumi.IntOutput {
	return o.ApplyT(func(v *LogmeCredential) pulumi.IntOutput { return v.Port }).(pulumi.IntOutput)
}

// STACKIT Project ID to which the instance is associated.
func (o LogmeCredentialOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v *LogmeCredential) pulumi.StringOutput { return v.ProjectId }).(pulumi.StringOutput)
}

func (o LogmeCredentialOutput) Uri() pulumi.StringOutput {
	return o.ApplyT(func(v *LogmeCredential) pulumi.StringOutput { return v.Uri }).(pulumi.StringOutput)
}

func (o LogmeCredentialOutput) Username() pulumi.StringOutput {
	return o.ApplyT(func(v *LogmeCredential) pulumi.StringOutput { return v.Username }).(pulumi.StringOutput)
}

type LogmeCredentialArrayOutput struct{ *pulumi.OutputState }

func (LogmeCredentialArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*LogmeCredential)(nil)).Elem()
}

func (o LogmeCredentialArrayOutput) ToLogmeCredentialArrayOutput() LogmeCredentialArrayOutput {
	return o
}

func (o LogmeCredentialArrayOutput) ToLogmeCredentialArrayOutputWithContext(ctx context.Context) LogmeCredentialArrayOutput {
	return o
}

func (o LogmeCredentialArrayOutput) Index(i pulumi.IntInput) LogmeCredentialOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *LogmeCredential {
		return vs[0].([]*LogmeCredential)[vs[1].(int)]
	}).(LogmeCredentialOutput)
}

type LogmeCredentialMapOutput struct{ *pulumi.OutputState }

func (LogmeCredentialMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*LogmeCredential)(nil)).Elem()
}

func (o LogmeCredentialMapOutput) ToLogmeCredentialMapOutput() LogmeCredentialMapOutput {
	return o
}

func (o LogmeCredentialMapOutput) ToLogmeCredentialMapOutputWithContext(ctx context.Context) LogmeCredentialMapOutput {
	return o
}

func (o LogmeCredentialMapOutput) MapIndex(k pulumi.StringInput) LogmeCredentialOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *LogmeCredential {
		return vs[0].(map[string]*LogmeCredential)[vs[1].(string)]
	}).(LogmeCredentialOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LogmeCredentialInput)(nil)).Elem(), &LogmeCredential{})
	pulumi.RegisterInputType(reflect.TypeOf((*LogmeCredentialArrayInput)(nil)).Elem(), LogmeCredentialArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*LogmeCredentialMapInput)(nil)).Elem(), LogmeCredentialMap{})
	pulumi.RegisterOutputType(LogmeCredentialOutput{})
	pulumi.RegisterOutputType(LogmeCredentialArrayOutput{})
	pulumi.RegisterOutputType(LogmeCredentialMapOutput{})
}
