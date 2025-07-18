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
func LookupSecurityGroupRule(ctx *pulumi.Context, args *LookupSecurityGroupRuleArgs, opts ...pulumi.InvokeOption) (*LookupSecurityGroupRuleResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupSecurityGroupRuleResult
	err := ctx.Invoke("stackit:index/getSecurityGroupRule:getSecurityGroupRule", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSecurityGroupRule.
type LookupSecurityGroupRuleArgs struct {
	// STACKIT project ID to which the security group rule is associated.
	ProjectId string `pulumi:"projectId"`
	// The security group ID.
	SecurityGroupId string `pulumi:"securityGroupId"`
	// The security group rule ID.
	SecurityGroupRuleId string `pulumi:"securityGroupRuleId"`
}

// A collection of values returned by getSecurityGroupRule.
type LookupSecurityGroupRuleResult struct {
	// The description of the security group rule.
	Description string `pulumi:"description"`
	// The direction of the traffic which the rule should match. Some of the possible values are: Supported values are: `ingress`, `egress`.
	Direction string `pulumi:"direction"`
	// The ethertype which the rule should match.
	EtherType string `pulumi:"etherType"`
	// ICMP Parameters.
	IcmpParameters GetSecurityGroupRuleIcmpParameters `pulumi:"icmpParameters"`
	Id             string                             `pulumi:"id"`
	// The remote IP range which the rule should match.
	IpRange string `pulumi:"ipRange"`
	// The range of ports.
	PortRange GetSecurityGroupRulePortRange `pulumi:"portRange"`
	// STACKIT project ID to which the security group rule is associated.
	ProjectId string `pulumi:"projectId"`
	// The internet protocol which the rule should match.
	Protocol GetSecurityGroupRuleProtocol `pulumi:"protocol"`
	// The remote security group which the rule should match.
	RemoteSecurityGroupId string `pulumi:"remoteSecurityGroupId"`
	// The security group ID.
	SecurityGroupId string `pulumi:"securityGroupId"`
	// The security group rule ID.
	SecurityGroupRuleId string `pulumi:"securityGroupRuleId"`
}

func LookupSecurityGroupRuleOutput(ctx *pulumi.Context, args LookupSecurityGroupRuleOutputArgs, opts ...pulumi.InvokeOption) LookupSecurityGroupRuleResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupSecurityGroupRuleResultOutput, error) {
			args := v.(LookupSecurityGroupRuleArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("stackit:index/getSecurityGroupRule:getSecurityGroupRule", args, LookupSecurityGroupRuleResultOutput{}, options).(LookupSecurityGroupRuleResultOutput), nil
		}).(LookupSecurityGroupRuleResultOutput)
}

// A collection of arguments for invoking getSecurityGroupRule.
type LookupSecurityGroupRuleOutputArgs struct {
	// STACKIT project ID to which the security group rule is associated.
	ProjectId pulumi.StringInput `pulumi:"projectId"`
	// The security group ID.
	SecurityGroupId pulumi.StringInput `pulumi:"securityGroupId"`
	// The security group rule ID.
	SecurityGroupRuleId pulumi.StringInput `pulumi:"securityGroupRuleId"`
}

func (LookupSecurityGroupRuleOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSecurityGroupRuleArgs)(nil)).Elem()
}

// A collection of values returned by getSecurityGroupRule.
type LookupSecurityGroupRuleResultOutput struct{ *pulumi.OutputState }

func (LookupSecurityGroupRuleResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSecurityGroupRuleResult)(nil)).Elem()
}

func (o LookupSecurityGroupRuleResultOutput) ToLookupSecurityGroupRuleResultOutput() LookupSecurityGroupRuleResultOutput {
	return o
}

func (o LookupSecurityGroupRuleResultOutput) ToLookupSecurityGroupRuleResultOutputWithContext(ctx context.Context) LookupSecurityGroupRuleResultOutput {
	return o
}

// The description of the security group rule.
func (o LookupSecurityGroupRuleResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityGroupRuleResult) string { return v.Description }).(pulumi.StringOutput)
}

// The direction of the traffic which the rule should match. Some of the possible values are: Supported values are: `ingress`, `egress`.
func (o LookupSecurityGroupRuleResultOutput) Direction() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityGroupRuleResult) string { return v.Direction }).(pulumi.StringOutput)
}

// The ethertype which the rule should match.
func (o LookupSecurityGroupRuleResultOutput) EtherType() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityGroupRuleResult) string { return v.EtherType }).(pulumi.StringOutput)
}

// ICMP Parameters.
func (o LookupSecurityGroupRuleResultOutput) IcmpParameters() GetSecurityGroupRuleIcmpParametersOutput {
	return o.ApplyT(func(v LookupSecurityGroupRuleResult) GetSecurityGroupRuleIcmpParameters { return v.IcmpParameters }).(GetSecurityGroupRuleIcmpParametersOutput)
}

func (o LookupSecurityGroupRuleResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityGroupRuleResult) string { return v.Id }).(pulumi.StringOutput)
}

// The remote IP range which the rule should match.
func (o LookupSecurityGroupRuleResultOutput) IpRange() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityGroupRuleResult) string { return v.IpRange }).(pulumi.StringOutput)
}

// The range of ports.
func (o LookupSecurityGroupRuleResultOutput) PortRange() GetSecurityGroupRulePortRangeOutput {
	return o.ApplyT(func(v LookupSecurityGroupRuleResult) GetSecurityGroupRulePortRange { return v.PortRange }).(GetSecurityGroupRulePortRangeOutput)
}

// STACKIT project ID to which the security group rule is associated.
func (o LookupSecurityGroupRuleResultOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityGroupRuleResult) string { return v.ProjectId }).(pulumi.StringOutput)
}

// The internet protocol which the rule should match.
func (o LookupSecurityGroupRuleResultOutput) Protocol() GetSecurityGroupRuleProtocolOutput {
	return o.ApplyT(func(v LookupSecurityGroupRuleResult) GetSecurityGroupRuleProtocol { return v.Protocol }).(GetSecurityGroupRuleProtocolOutput)
}

// The remote security group which the rule should match.
func (o LookupSecurityGroupRuleResultOutput) RemoteSecurityGroupId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityGroupRuleResult) string { return v.RemoteSecurityGroupId }).(pulumi.StringOutput)
}

// The security group ID.
func (o LookupSecurityGroupRuleResultOutput) SecurityGroupId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityGroupRuleResult) string { return v.SecurityGroupId }).(pulumi.StringOutput)
}

// The security group rule ID.
func (o LookupSecurityGroupRuleResultOutput) SecurityGroupRuleId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSecurityGroupRuleResult) string { return v.SecurityGroupRuleId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSecurityGroupRuleResultOutput{})
}
