// Code generated by pulumi-language-go DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package stackit

import (
	"context"
	"reflect"

	"github.com/dirien/pulumi-stackit/sdk/go/stackit/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Network area datasource schema. Must have a `region` specified in the provider configuration.
//
// ## Example Usage
func LookupNetworkArea(ctx *pulumi.Context, args *LookupNetworkAreaArgs, opts ...pulumi.InvokeOption) (*LookupNetworkAreaResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupNetworkAreaResult
	err := ctx.Invoke("stackit:index/getNetworkArea:getNetworkArea", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNetworkArea.
type LookupNetworkAreaArgs struct {
	// The network area ID.
	NetworkAreaId string `pulumi:"networkAreaId"`
	// STACKIT organization ID to which the network area is associated.
	OrganizationId string `pulumi:"organizationId"`
}

// A collection of values returned by getNetworkArea.
type LookupNetworkAreaResult struct {
	// List of DNS Servers/Nameservers.
	DefaultNameservers []string `pulumi:"defaultNameservers"`
	// The default prefix length for networks in the network area.
	DefaultPrefixLength int    `pulumi:"defaultPrefixLength"`
	Id                  string `pulumi:"id"`
	// Labels are key-value string pairs which can be attached to a resource container
	Labels map[string]string `pulumi:"labels"`
	// The maximal prefix length for networks in the network area.
	MaxPrefixLength int `pulumi:"maxPrefixLength"`
	// The minimal prefix length for networks in the network area.
	MinPrefixLength int `pulumi:"minPrefixLength"`
	// The name of the network area.
	Name string `pulumi:"name"`
	// The network area ID.
	NetworkAreaId string `pulumi:"networkAreaId"`
	// List of Network ranges.
	NetworkRanges []GetNetworkAreaNetworkRange `pulumi:"networkRanges"`
	// STACKIT organization ID to which the network area is associated.
	OrganizationId string `pulumi:"organizationId"`
	// The amount of projects currently referencing this area.
	ProjectCount int `pulumi:"projectCount"`
	// Classless Inter-Domain Routing (CIDR).
	TransferNetwork string `pulumi:"transferNetwork"`
}

func LookupNetworkAreaOutput(ctx *pulumi.Context, args LookupNetworkAreaOutputArgs, opts ...pulumi.InvokeOption) LookupNetworkAreaResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (LookupNetworkAreaResultOutput, error) {
			args := v.(LookupNetworkAreaArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("stackit:index/getNetworkArea:getNetworkArea", args, LookupNetworkAreaResultOutput{}, options).(LookupNetworkAreaResultOutput), nil
		}).(LookupNetworkAreaResultOutput)
}

// A collection of arguments for invoking getNetworkArea.
type LookupNetworkAreaOutputArgs struct {
	// The network area ID.
	NetworkAreaId pulumi.StringInput `pulumi:"networkAreaId"`
	// STACKIT organization ID to which the network area is associated.
	OrganizationId pulumi.StringInput `pulumi:"organizationId"`
}

func (LookupNetworkAreaOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkAreaArgs)(nil)).Elem()
}

// A collection of values returned by getNetworkArea.
type LookupNetworkAreaResultOutput struct{ *pulumi.OutputState }

func (LookupNetworkAreaResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkAreaResult)(nil)).Elem()
}

func (o LookupNetworkAreaResultOutput) ToLookupNetworkAreaResultOutput() LookupNetworkAreaResultOutput {
	return o
}

func (o LookupNetworkAreaResultOutput) ToLookupNetworkAreaResultOutputWithContext(ctx context.Context) LookupNetworkAreaResultOutput {
	return o
}

// List of DNS Servers/Nameservers.
func (o LookupNetworkAreaResultOutput) DefaultNameservers() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupNetworkAreaResult) []string { return v.DefaultNameservers }).(pulumi.StringArrayOutput)
}

// The default prefix length for networks in the network area.
func (o LookupNetworkAreaResultOutput) DefaultPrefixLength() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNetworkAreaResult) int { return v.DefaultPrefixLength }).(pulumi.IntOutput)
}

func (o LookupNetworkAreaResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNetworkAreaResult) string { return v.Id }).(pulumi.StringOutput)
}

// Labels are key-value string pairs which can be attached to a resource container
func (o LookupNetworkAreaResultOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupNetworkAreaResult) map[string]string { return v.Labels }).(pulumi.StringMapOutput)
}

// The maximal prefix length for networks in the network area.
func (o LookupNetworkAreaResultOutput) MaxPrefixLength() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNetworkAreaResult) int { return v.MaxPrefixLength }).(pulumi.IntOutput)
}

// The minimal prefix length for networks in the network area.
func (o LookupNetworkAreaResultOutput) MinPrefixLength() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNetworkAreaResult) int { return v.MinPrefixLength }).(pulumi.IntOutput)
}

// The name of the network area.
func (o LookupNetworkAreaResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNetworkAreaResult) string { return v.Name }).(pulumi.StringOutput)
}

// The network area ID.
func (o LookupNetworkAreaResultOutput) NetworkAreaId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNetworkAreaResult) string { return v.NetworkAreaId }).(pulumi.StringOutput)
}

// List of Network ranges.
func (o LookupNetworkAreaResultOutput) NetworkRanges() GetNetworkAreaNetworkRangeArrayOutput {
	return o.ApplyT(func(v LookupNetworkAreaResult) []GetNetworkAreaNetworkRange { return v.NetworkRanges }).(GetNetworkAreaNetworkRangeArrayOutput)
}

// STACKIT organization ID to which the network area is associated.
func (o LookupNetworkAreaResultOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNetworkAreaResult) string { return v.OrganizationId }).(pulumi.StringOutput)
}

// The amount of projects currently referencing this area.
func (o LookupNetworkAreaResultOutput) ProjectCount() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNetworkAreaResult) int { return v.ProjectCount }).(pulumi.IntOutput)
}

// Classless Inter-Domain Routing (CIDR).
func (o LookupNetworkAreaResultOutput) TransferNetwork() pulumi.StringOutput {
	return o.ApplyT(func(v LookupNetworkAreaResult) string { return v.TransferNetwork }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNetworkAreaResultOutput{})
}
