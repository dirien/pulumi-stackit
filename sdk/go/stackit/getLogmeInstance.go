// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package stackit

import (
	"context"
	"reflect"

	"github.com/dirien/pulumi-stackit/sdk/go/stackit/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// LogMe instance data source schema. Must have a `region` specified in the provider configuration.
//
// ## Example Usage
func LookupLogmeInstance(ctx *pulumi.Context, args *LookupLogmeInstanceArgs, opts ...pulumi.InvokeOption) (*LookupLogmeInstanceResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupLogmeInstanceResult
	err := ctx.Invoke("stackit:index/getLogmeInstance:getLogmeInstance", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getLogmeInstance.
type LookupLogmeInstanceArgs struct {
	// ID of the LogMe instance.
	InstanceId string `pulumi:"instanceId"`
	// STACKIT Project ID to which the instance is associated.
	ProjectId string `pulumi:"projectId"`
}

// A collection of values returned by getLogmeInstance.
type LookupLogmeInstanceResult struct {
	CfGuid             string `pulumi:"cfGuid"`
	CfOrganizationGuid string `pulumi:"cfOrganizationGuid"`
	CfSpaceGuid        string `pulumi:"cfSpaceGuid"`
	DashboardUrl       string `pulumi:"dashboardUrl"`
	Id                 string `pulumi:"id"`
	ImageUrl           string `pulumi:"imageUrl"`
	// ID of the LogMe instance.
	InstanceId string `pulumi:"instanceId"`
	// Instance name.
	Name       string                     `pulumi:"name"`
	Parameters GetLogmeInstanceParameters `pulumi:"parameters"`
	// The selected plan ID.
	PlanId string `pulumi:"planId"`
	// The selected plan name.
	PlanName string `pulumi:"planName"`
	// STACKIT Project ID to which the instance is associated.
	ProjectId string `pulumi:"projectId"`
	// The service version.
	Version string `pulumi:"version"`
}

func LookupLogmeInstanceOutput(ctx *pulumi.Context, args LookupLogmeInstanceOutputArgs, opts ...pulumi.InvokeOption) LookupLogmeInstanceResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupLogmeInstanceResultOutput, error) {
			args := v.(LookupLogmeInstanceArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("stackit:index/getLogmeInstance:getLogmeInstance", args, LookupLogmeInstanceResultOutput{}, options).(LookupLogmeInstanceResultOutput), nil
		}).(LookupLogmeInstanceResultOutput)
}

// A collection of arguments for invoking getLogmeInstance.
type LookupLogmeInstanceOutputArgs struct {
	// ID of the LogMe instance.
	InstanceId pulumi.StringInput `pulumi:"instanceId"`
	// STACKIT Project ID to which the instance is associated.
	ProjectId pulumi.StringInput `pulumi:"projectId"`
}

func (LookupLogmeInstanceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLogmeInstanceArgs)(nil)).Elem()
}

// A collection of values returned by getLogmeInstance.
type LookupLogmeInstanceResultOutput struct{ *pulumi.OutputState }

func (LookupLogmeInstanceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLogmeInstanceResult)(nil)).Elem()
}

func (o LookupLogmeInstanceResultOutput) ToLookupLogmeInstanceResultOutput() LookupLogmeInstanceResultOutput {
	return o
}

func (o LookupLogmeInstanceResultOutput) ToLookupLogmeInstanceResultOutputWithContext(ctx context.Context) LookupLogmeInstanceResultOutput {
	return o
}

func (o LookupLogmeInstanceResultOutput) CfGuid() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogmeInstanceResult) string { return v.CfGuid }).(pulumi.StringOutput)
}

func (o LookupLogmeInstanceResultOutput) CfOrganizationGuid() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogmeInstanceResult) string { return v.CfOrganizationGuid }).(pulumi.StringOutput)
}

func (o LookupLogmeInstanceResultOutput) CfSpaceGuid() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogmeInstanceResult) string { return v.CfSpaceGuid }).(pulumi.StringOutput)
}

func (o LookupLogmeInstanceResultOutput) DashboardUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogmeInstanceResult) string { return v.DashboardUrl }).(pulumi.StringOutput)
}

func (o LookupLogmeInstanceResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogmeInstanceResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupLogmeInstanceResultOutput) ImageUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogmeInstanceResult) string { return v.ImageUrl }).(pulumi.StringOutput)
}

// ID of the LogMe instance.
func (o LookupLogmeInstanceResultOutput) InstanceId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogmeInstanceResult) string { return v.InstanceId }).(pulumi.StringOutput)
}

// Instance name.
func (o LookupLogmeInstanceResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogmeInstanceResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupLogmeInstanceResultOutput) Parameters() GetLogmeInstanceParametersOutput {
	return o.ApplyT(func(v LookupLogmeInstanceResult) GetLogmeInstanceParameters { return v.Parameters }).(GetLogmeInstanceParametersOutput)
}

// The selected plan ID.
func (o LookupLogmeInstanceResultOutput) PlanId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogmeInstanceResult) string { return v.PlanId }).(pulumi.StringOutput)
}

// The selected plan name.
func (o LookupLogmeInstanceResultOutput) PlanName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogmeInstanceResult) string { return v.PlanName }).(pulumi.StringOutput)
}

// STACKIT Project ID to which the instance is associated.
func (o LookupLogmeInstanceResultOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogmeInstanceResult) string { return v.ProjectId }).(pulumi.StringOutput)
}

// The service version.
func (o LookupLogmeInstanceResultOutput) Version() pulumi.StringOutput {
	return o.ApplyT(func(v LookupLogmeInstanceResult) string { return v.Version }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLogmeInstanceResultOutput{})
}
