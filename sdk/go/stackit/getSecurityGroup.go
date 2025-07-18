// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package stackit

import (
	"context"
	"reflect"

	"github.com/dirien/pulumi-stackit/sdk/go/stackit/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Security group datasource schema. Must have a `region` specified in the provider configuration.
//
// ## Example Usage
func LookupSecurityGroup(ctx *pulumi.Context, args *LookupSecurityGroupArgs, opts ...pulumi.InvokeOption) (*LookupSecurityGroupResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupSecurityGroupResult
	err := ctx.Invoke("stackit:index/getSecurityGroup:getSecurityGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSecurityGroup.
type LookupSecurityGroupArgs struct {
	// STACKIT project ID to which the security group is associated.
	ProjectId string `pulumi:"projectId"`
	// The security group ID.
	SecurityGroupId string `pulumi:"securityGroupId"`
}

// A collection of values returned by getSecurityGroup.
type LookupSecurityGroupResult struct {
	// The description of the security group.
	Description string `pulumi:"description"`
	Id          string `pulumi:"id"`
	// Labels are key-value string pairs which can be attached to a resource container
	Labels map[string]string `pulumi:"labels"`
	// The name of the security group.
	Name string `pulumi:"name"`
	// STACKIT project ID to which the security group is associated.
	ProjectId string `pulumi:"projectId"`
	// The security group ID.
	SecurityGroupId string `pulumi:"securityGroupId"`
	// Configures if a security group is stateful or stateless. There can only be one type of security groups per network interface/server.
	Stateful bool `pulumi:"stateful"`
}

func LookupSecurityGroupOutput(ctx *pulumi.Context, args LookupSecurityGroupOutputArgs, opts ...pulumi.InvokeOption) LookupSecurityGroupResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupSecurityGroupResultOutput, error) {
			args := v.(LookupSecurityGroupArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("stackit:index/getSecurityGroup:getSecurityGroup", args, LookupSecurityGroupResultOutput{}, options).(LookupSecurityGroupResultOutput), nil
		}).(LookupSecurityGroupResultOutput)
}

// A collection of arguments for invoking getSecurityGroup.
type LookupSecurityGroupOutputArgs struct {
	// STACKIT project ID to which the security group is associated.
	ProjectId pulumi.StringInput `pulumi:"projectId"`
	// The security group ID.
	SecurityGroupId pulumi.StringInput `pulumi:"securityGroupId"`
}

func (LookupSecurityGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSecurityGroupArgs)(nil)).Elem()
}

// A collection of values returned by getSecurityGroup.
type LookupSecurityGroupResultOutput struct{ *pulumi.OutputState }

func (LookupSecurityGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSecurityGroupResult)(nil)).Elem()
}

func (o LookupSecurityGroupResultOutput) ToLookupSecurityGroupResultOutput() LookupSecurityGroupResultOutput {
	return o
}

func (o LookupSecurityGroupResultOutput) ToLookupSecurityGroupResultOutputWithContext(ctx context.Context) LookupSecurityGroupResultOutput {
	return o
}

// The description of the security group.
func (o LookupSecurityGroupResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityGroupResult) string { return v.Description }).(pulumi.StringOutput)
}

func (o LookupSecurityGroupResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityGroupResult) string { return v.Id }).(pulumi.StringOutput)
}

// Labels are key-value string pairs which can be attached to a resource container
func (o LookupSecurityGroupResultOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupSecurityGroupResult) map[string]string { return v.Labels }).(pulumi.StringMapOutput)
}

// The name of the security group.
func (o LookupSecurityGroupResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityGroupResult) string { return v.Name }).(pulumi.StringOutput)
}

// STACKIT project ID to which the security group is associated.
func (o LookupSecurityGroupResultOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityGroupResult) string { return v.ProjectId }).(pulumi.StringOutput)
}

// The security group ID.
func (o LookupSecurityGroupResultOutput) SecurityGroupId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityGroupResult) string { return v.SecurityGroupId }).(pulumi.StringOutput)
}

// Configures if a security group is stateful or stateless. There can only be one type of security groups per network interface/server.
func (o LookupSecurityGroupResultOutput) Stateful() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupSecurityGroupResult) bool { return v.Stateful }).(pulumi.BoolOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSecurityGroupResultOutput{})
}
