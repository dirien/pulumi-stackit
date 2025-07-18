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

// Affinity Group schema. Must have a `region` specified in the provider configuration.
//
// ## Example Usage
type AffinityGroup struct {
	pulumi.CustomResourceState

	// The affinity group ID.
	AffinityGroupId pulumi.StringOutput `pulumi:"affinityGroupId"`
	// The servers that are part of the affinity group.
	Members pulumi.StringArrayOutput `pulumi:"members"`
	// The name of the affinity group.
	Name pulumi.StringOutput `pulumi:"name"`
	// The policy of the affinity group.
	Policy pulumi.StringOutput `pulumi:"policy"`
	// STACKIT Project ID to which the affinity group is associated.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
}

// NewAffinityGroup registers a new resource with the given unique name, arguments, and options.
func NewAffinityGroup(ctx *pulumi.Context,
	name string, args *AffinityGroupArgs, opts ...pulumi.ResourceOption) (*AffinityGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Policy == nil {
		return nil, errors.New("invalid value for required argument 'Policy'")
	}
	if args.ProjectId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource AffinityGroup
	err := ctx.RegisterResource("stackit:index/affinityGroup:AffinityGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAffinityGroup gets an existing AffinityGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAffinityGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AffinityGroupState, opts ...pulumi.ResourceOption) (*AffinityGroup, error) {
	var resource AffinityGroup
	err := ctx.ReadResource("stackit:index/affinityGroup:AffinityGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AffinityGroup resources.
type affinityGroupState struct {
	// The affinity group ID.
	AffinityGroupId *string `pulumi:"affinityGroupId"`
	// The servers that are part of the affinity group.
	Members []string `pulumi:"members"`
	// The name of the affinity group.
	Name *string `pulumi:"name"`
	// The policy of the affinity group.
	Policy *string `pulumi:"policy"`
	// STACKIT Project ID to which the affinity group is associated.
	ProjectId *string `pulumi:"projectId"`
}

type AffinityGroupState struct {
	// The affinity group ID.
	AffinityGroupId pulumi.StringPtrInput
	// The servers that are part of the affinity group.
	Members pulumi.StringArrayInput
	// The name of the affinity group.
	Name pulumi.StringPtrInput
	// The policy of the affinity group.
	Policy pulumi.StringPtrInput
	// STACKIT Project ID to which the affinity group is associated.
	ProjectId pulumi.StringPtrInput
}

func (AffinityGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*affinityGroupState)(nil)).Elem()
}

type affinityGroupArgs struct {
	// The name of the affinity group.
	Name *string `pulumi:"name"`
	// The policy of the affinity group.
	Policy string `pulumi:"policy"`
	// STACKIT Project ID to which the affinity group is associated.
	ProjectId string `pulumi:"projectId"`
}

// The set of arguments for constructing a AffinityGroup resource.
type AffinityGroupArgs struct {
	// The name of the affinity group.
	Name pulumi.StringPtrInput
	// The policy of the affinity group.
	Policy pulumi.StringInput
	// STACKIT Project ID to which the affinity group is associated.
	ProjectId pulumi.StringInput
}

func (AffinityGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*affinityGroupArgs)(nil)).Elem()
}

type AffinityGroupInput interface {
	pulumi.Input

	ToAffinityGroupOutput() AffinityGroupOutput
	ToAffinityGroupOutputWithContext(ctx context.Context) AffinityGroupOutput
}

func (*AffinityGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**AffinityGroup)(nil)).Elem()
}

func (i *AffinityGroup) ToAffinityGroupOutput() AffinityGroupOutput {
	return i.ToAffinityGroupOutputWithContext(context.Background())
}

func (i *AffinityGroup) ToAffinityGroupOutputWithContext(ctx context.Context) AffinityGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AffinityGroupOutput)
}

// AffinityGroupArrayInput is an input type that accepts AffinityGroupArray and AffinityGroupArrayOutput values.
// You can construct a concrete instance of `AffinityGroupArrayInput` via:
//
//	AffinityGroupArray{ AffinityGroupArgs{...} }
type AffinityGroupArrayInput interface {
	pulumi.Input

	ToAffinityGroupArrayOutput() AffinityGroupArrayOutput
	ToAffinityGroupArrayOutputWithContext(context.Context) AffinityGroupArrayOutput
}

type AffinityGroupArray []AffinityGroupInput

func (AffinityGroupArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AffinityGroup)(nil)).Elem()
}

func (i AffinityGroupArray) ToAffinityGroupArrayOutput() AffinityGroupArrayOutput {
	return i.ToAffinityGroupArrayOutputWithContext(context.Background())
}

func (i AffinityGroupArray) ToAffinityGroupArrayOutputWithContext(ctx context.Context) AffinityGroupArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AffinityGroupArrayOutput)
}

// AffinityGroupMapInput is an input type that accepts AffinityGroupMap and AffinityGroupMapOutput values.
// You can construct a concrete instance of `AffinityGroupMapInput` via:
//
//	AffinityGroupMap{ "key": AffinityGroupArgs{...} }
type AffinityGroupMapInput interface {
	pulumi.Input

	ToAffinityGroupMapOutput() AffinityGroupMapOutput
	ToAffinityGroupMapOutputWithContext(context.Context) AffinityGroupMapOutput
}

type AffinityGroupMap map[string]AffinityGroupInput

func (AffinityGroupMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AffinityGroup)(nil)).Elem()
}

func (i AffinityGroupMap) ToAffinityGroupMapOutput() AffinityGroupMapOutput {
	return i.ToAffinityGroupMapOutputWithContext(context.Background())
}

func (i AffinityGroupMap) ToAffinityGroupMapOutputWithContext(ctx context.Context) AffinityGroupMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AffinityGroupMapOutput)
}

type AffinityGroupOutput struct{ *pulumi.OutputState }

func (AffinityGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AffinityGroup)(nil)).Elem()
}

func (o AffinityGroupOutput) ToAffinityGroupOutput() AffinityGroupOutput {
	return o
}

func (o AffinityGroupOutput) ToAffinityGroupOutputWithContext(ctx context.Context) AffinityGroupOutput {
	return o
}

// The affinity group ID.
func (o AffinityGroupOutput) AffinityGroupId() pulumi.StringOutput {
	return o.ApplyT(func(v *AffinityGroup) pulumi.StringOutput { return v.AffinityGroupId }).(pulumi.StringOutput)
}

// The servers that are part of the affinity group.
func (o AffinityGroupOutput) Members() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *AffinityGroup) pulumi.StringArrayOutput { return v.Members }).(pulumi.StringArrayOutput)
}

// The name of the affinity group.
func (o AffinityGroupOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *AffinityGroup) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The policy of the affinity group.
func (o AffinityGroupOutput) Policy() pulumi.StringOutput {
	return o.ApplyT(func(v *AffinityGroup) pulumi.StringOutput { return v.Policy }).(pulumi.StringOutput)
}

// STACKIT Project ID to which the affinity group is associated.
func (o AffinityGroupOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v *AffinityGroup) pulumi.StringOutput { return v.ProjectId }).(pulumi.StringOutput)
}

type AffinityGroupArrayOutput struct{ *pulumi.OutputState }

func (AffinityGroupArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AffinityGroup)(nil)).Elem()
}

func (o AffinityGroupArrayOutput) ToAffinityGroupArrayOutput() AffinityGroupArrayOutput {
	return o
}

func (o AffinityGroupArrayOutput) ToAffinityGroupArrayOutputWithContext(ctx context.Context) AffinityGroupArrayOutput {
	return o
}

func (o AffinityGroupArrayOutput) Index(i pulumi.IntInput) AffinityGroupOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *AffinityGroup {
		return vs[0].([]*AffinityGroup)[vs[1].(int)]
	}).(AffinityGroupOutput)
}

type AffinityGroupMapOutput struct{ *pulumi.OutputState }

func (AffinityGroupMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AffinityGroup)(nil)).Elem()
}

func (o AffinityGroupMapOutput) ToAffinityGroupMapOutput() AffinityGroupMapOutput {
	return o
}

func (o AffinityGroupMapOutput) ToAffinityGroupMapOutputWithContext(ctx context.Context) AffinityGroupMapOutput {
	return o
}

func (o AffinityGroupMapOutput) MapIndex(k pulumi.StringInput) AffinityGroupOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *AffinityGroup {
		return vs[0].(map[string]*AffinityGroup)[vs[1].(string)]
	}).(AffinityGroupOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AffinityGroupInput)(nil)).Elem(), &AffinityGroup{})
	pulumi.RegisterInputType(reflect.TypeOf((*AffinityGroupArrayInput)(nil)).Elem(), AffinityGroupArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AffinityGroupMapInput)(nil)).Elem(), AffinityGroupMap{})
	pulumi.RegisterOutputType(AffinityGroupOutput{})
	pulumi.RegisterOutputType(AffinityGroupArrayOutput{})
	pulumi.RegisterOutputType(AffinityGroupMapOutput{})
}
