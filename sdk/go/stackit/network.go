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

// Network resource schema. Must have a `region` specified in the provider configuration.
//
// ## Example Usage
type Network struct {
	pulumi.CustomResourceState

	// The IPv4 gateway of a network. If not specified, the first IP of the network will be assigned as the gateway.
	Ipv4Gateway pulumi.StringOutput `pulumi:"ipv4Gateway"`
	// The IPv4 nameservers of the network.
	Ipv4Nameservers pulumi.StringArrayOutput `pulumi:"ipv4Nameservers"`
	// The IPv4 prefix of the network (CIDR).
	Ipv4Prefix pulumi.StringOutput `pulumi:"ipv4Prefix"`
	// The IPv4 prefix length of the network.
	Ipv4PrefixLength pulumi.IntOutput `pulumi:"ipv4PrefixLength"`
	// The IPv4 prefixes of the network.
	Ipv4Prefixes pulumi.StringArrayOutput `pulumi:"ipv4Prefixes"`
	// The IPv6 gateway of a network. If not specified, the first IP of the network will be assigned as the gateway.
	Ipv6Gateway pulumi.StringOutput `pulumi:"ipv6Gateway"`
	// The IPv6 nameservers of the network.
	Ipv6Nameservers pulumi.StringArrayOutput `pulumi:"ipv6Nameservers"`
	// The IPv6 prefix of the network (CIDR).
	Ipv6Prefix pulumi.StringPtrOutput `pulumi:"ipv6Prefix"`
	// The IPv6 prefix length of the network.
	Ipv6PrefixLength pulumi.IntPtrOutput `pulumi:"ipv6PrefixLength"`
	// The IPv6 prefixes of the network.
	Ipv6Prefixes pulumi.StringArrayOutput `pulumi:"ipv6Prefixes"`
	// Labels are key-value string pairs which can be attached to a resource container
	Labels pulumi.StringMapOutput `pulumi:"labels"`
	// The name of the network.
	Name pulumi.StringOutput `pulumi:"name"`
	// The nameservers of the network. This field is deprecated and will be removed soon, use `ipv4Nameservers` to configure the nameservers for IPv4.
	//
	// Deprecated: Use `ipv4Nameservers` to configure the nameservers for IPv4.
	Nameservers pulumi.StringArrayOutput `pulumi:"nameservers"`
	// The network ID.
	NetworkId pulumi.StringOutput `pulumi:"networkId"`
	// If set to `true`, the network doesn't have a gateway.
	NoIpv4Gateway pulumi.BoolPtrOutput `pulumi:"noIpv4Gateway"`
	// If set to `true`, the network doesn't have a gateway.
	NoIpv6Gateway pulumi.BoolPtrOutput `pulumi:"noIpv6Gateway"`
	// The prefixes of the network. This field is deprecated and will be removed soon, use `ipv4Prefixes` to read the prefixes of the IPv4 networks.
	//
	// Deprecated: Use `ipv4Prefixes` to read the prefixes of the IPv4 networks.
	Prefixes pulumi.StringArrayOutput `pulumi:"prefixes"`
	// STACKIT project ID to which the network is associated.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// The public IP of the network.
	PublicIp pulumi.StringOutput `pulumi:"publicIp"`
	// If set to `true`, the network is routed and therefore accessible from other networks.
	Routed pulumi.BoolOutput `pulumi:"routed"`
}

// NewNetwork registers a new resource with the given unique name, arguments, and options.
func NewNetwork(ctx *pulumi.Context,
	name string, args *NetworkArgs, opts ...pulumi.ResourceOption) (*Network, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ProjectId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Network
	err := ctx.RegisterResource("stackit:index/network:Network", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNetwork gets an existing Network resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetwork(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NetworkState, opts ...pulumi.ResourceOption) (*Network, error) {
	var resource Network
	err := ctx.ReadResource("stackit:index/network:Network", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Network resources.
type networkState struct {
	// The IPv4 gateway of a network. If not specified, the first IP of the network will be assigned as the gateway.
	Ipv4Gateway *string `pulumi:"ipv4Gateway"`
	// The IPv4 nameservers of the network.
	Ipv4Nameservers []string `pulumi:"ipv4Nameservers"`
	// The IPv4 prefix of the network (CIDR).
	Ipv4Prefix *string `pulumi:"ipv4Prefix"`
	// The IPv4 prefix length of the network.
	Ipv4PrefixLength *int `pulumi:"ipv4PrefixLength"`
	// The IPv4 prefixes of the network.
	Ipv4Prefixes []string `pulumi:"ipv4Prefixes"`
	// The IPv6 gateway of a network. If not specified, the first IP of the network will be assigned as the gateway.
	Ipv6Gateway *string `pulumi:"ipv6Gateway"`
	// The IPv6 nameservers of the network.
	Ipv6Nameservers []string `pulumi:"ipv6Nameservers"`
	// The IPv6 prefix of the network (CIDR).
	Ipv6Prefix *string `pulumi:"ipv6Prefix"`
	// The IPv6 prefix length of the network.
	Ipv6PrefixLength *int `pulumi:"ipv6PrefixLength"`
	// The IPv6 prefixes of the network.
	Ipv6Prefixes []string `pulumi:"ipv6Prefixes"`
	// Labels are key-value string pairs which can be attached to a resource container
	Labels map[string]string `pulumi:"labels"`
	// The name of the network.
	Name *string `pulumi:"name"`
	// The nameservers of the network. This field is deprecated and will be removed soon, use `ipv4Nameservers` to configure the nameservers for IPv4.
	//
	// Deprecated: Use `ipv4Nameservers` to configure the nameservers for IPv4.
	Nameservers []string `pulumi:"nameservers"`
	// The network ID.
	NetworkId *string `pulumi:"networkId"`
	// If set to `true`, the network doesn't have a gateway.
	NoIpv4Gateway *bool `pulumi:"noIpv4Gateway"`
	// If set to `true`, the network doesn't have a gateway.
	NoIpv6Gateway *bool `pulumi:"noIpv6Gateway"`
	// The prefixes of the network. This field is deprecated and will be removed soon, use `ipv4Prefixes` to read the prefixes of the IPv4 networks.
	//
	// Deprecated: Use `ipv4Prefixes` to read the prefixes of the IPv4 networks.
	Prefixes []string `pulumi:"prefixes"`
	// STACKIT project ID to which the network is associated.
	ProjectId *string `pulumi:"projectId"`
	// The public IP of the network.
	PublicIp *string `pulumi:"publicIp"`
	// If set to `true`, the network is routed and therefore accessible from other networks.
	Routed *bool `pulumi:"routed"`
}

type NetworkState struct {
	// The IPv4 gateway of a network. If not specified, the first IP of the network will be assigned as the gateway.
	Ipv4Gateway pulumi.StringPtrInput
	// The IPv4 nameservers of the network.
	Ipv4Nameservers pulumi.StringArrayInput
	// The IPv4 prefix of the network (CIDR).
	Ipv4Prefix pulumi.StringPtrInput
	// The IPv4 prefix length of the network.
	Ipv4PrefixLength pulumi.IntPtrInput
	// The IPv4 prefixes of the network.
	Ipv4Prefixes pulumi.StringArrayInput
	// The IPv6 gateway of a network. If not specified, the first IP of the network will be assigned as the gateway.
	Ipv6Gateway pulumi.StringPtrInput
	// The IPv6 nameservers of the network.
	Ipv6Nameservers pulumi.StringArrayInput
	// The IPv6 prefix of the network (CIDR).
	Ipv6Prefix pulumi.StringPtrInput
	// The IPv6 prefix length of the network.
	Ipv6PrefixLength pulumi.IntPtrInput
	// The IPv6 prefixes of the network.
	Ipv6Prefixes pulumi.StringArrayInput
	// Labels are key-value string pairs which can be attached to a resource container
	Labels pulumi.StringMapInput
	// The name of the network.
	Name pulumi.StringPtrInput
	// The nameservers of the network. This field is deprecated and will be removed soon, use `ipv4Nameservers` to configure the nameservers for IPv4.
	//
	// Deprecated: Use `ipv4Nameservers` to configure the nameservers for IPv4.
	Nameservers pulumi.StringArrayInput
	// The network ID.
	NetworkId pulumi.StringPtrInput
	// If set to `true`, the network doesn't have a gateway.
	NoIpv4Gateway pulumi.BoolPtrInput
	// If set to `true`, the network doesn't have a gateway.
	NoIpv6Gateway pulumi.BoolPtrInput
	// The prefixes of the network. This field is deprecated and will be removed soon, use `ipv4Prefixes` to read the prefixes of the IPv4 networks.
	//
	// Deprecated: Use `ipv4Prefixes` to read the prefixes of the IPv4 networks.
	Prefixes pulumi.StringArrayInput
	// STACKIT project ID to which the network is associated.
	ProjectId pulumi.StringPtrInput
	// The public IP of the network.
	PublicIp pulumi.StringPtrInput
	// If set to `true`, the network is routed and therefore accessible from other networks.
	Routed pulumi.BoolPtrInput
}

func (NetworkState) ElementType() reflect.Type {
	return reflect.TypeOf((*networkState)(nil)).Elem()
}

type networkArgs struct {
	// The IPv4 gateway of a network. If not specified, the first IP of the network will be assigned as the gateway.
	Ipv4Gateway *string `pulumi:"ipv4Gateway"`
	// The IPv4 nameservers of the network.
	Ipv4Nameservers []string `pulumi:"ipv4Nameservers"`
	// The IPv4 prefix of the network (CIDR).
	Ipv4Prefix *string `pulumi:"ipv4Prefix"`
	// The IPv4 prefix length of the network.
	Ipv4PrefixLength *int `pulumi:"ipv4PrefixLength"`
	// The IPv6 gateway of a network. If not specified, the first IP of the network will be assigned as the gateway.
	Ipv6Gateway *string `pulumi:"ipv6Gateway"`
	// The IPv6 nameservers of the network.
	Ipv6Nameservers []string `pulumi:"ipv6Nameservers"`
	// The IPv6 prefix of the network (CIDR).
	Ipv6Prefix *string `pulumi:"ipv6Prefix"`
	// The IPv6 prefix length of the network.
	Ipv6PrefixLength *int `pulumi:"ipv6PrefixLength"`
	// Labels are key-value string pairs which can be attached to a resource container
	Labels map[string]string `pulumi:"labels"`
	// The name of the network.
	Name *string `pulumi:"name"`
	// The nameservers of the network. This field is deprecated and will be removed soon, use `ipv4Nameservers` to configure the nameservers for IPv4.
	//
	// Deprecated: Use `ipv4Nameservers` to configure the nameservers for IPv4.
	Nameservers []string `pulumi:"nameservers"`
	// If set to `true`, the network doesn't have a gateway.
	NoIpv4Gateway *bool `pulumi:"noIpv4Gateway"`
	// If set to `true`, the network doesn't have a gateway.
	NoIpv6Gateway *bool `pulumi:"noIpv6Gateway"`
	// STACKIT project ID to which the network is associated.
	ProjectId string `pulumi:"projectId"`
	// If set to `true`, the network is routed and therefore accessible from other networks.
	Routed *bool `pulumi:"routed"`
}

// The set of arguments for constructing a Network resource.
type NetworkArgs struct {
	// The IPv4 gateway of a network. If not specified, the first IP of the network will be assigned as the gateway.
	Ipv4Gateway pulumi.StringPtrInput
	// The IPv4 nameservers of the network.
	Ipv4Nameservers pulumi.StringArrayInput
	// The IPv4 prefix of the network (CIDR).
	Ipv4Prefix pulumi.StringPtrInput
	// The IPv4 prefix length of the network.
	Ipv4PrefixLength pulumi.IntPtrInput
	// The IPv6 gateway of a network. If not specified, the first IP of the network will be assigned as the gateway.
	Ipv6Gateway pulumi.StringPtrInput
	// The IPv6 nameservers of the network.
	Ipv6Nameservers pulumi.StringArrayInput
	// The IPv6 prefix of the network (CIDR).
	Ipv6Prefix pulumi.StringPtrInput
	// The IPv6 prefix length of the network.
	Ipv6PrefixLength pulumi.IntPtrInput
	// Labels are key-value string pairs which can be attached to a resource container
	Labels pulumi.StringMapInput
	// The name of the network.
	Name pulumi.StringPtrInput
	// The nameservers of the network. This field is deprecated and will be removed soon, use `ipv4Nameservers` to configure the nameservers for IPv4.
	//
	// Deprecated: Use `ipv4Nameservers` to configure the nameservers for IPv4.
	Nameservers pulumi.StringArrayInput
	// If set to `true`, the network doesn't have a gateway.
	NoIpv4Gateway pulumi.BoolPtrInput
	// If set to `true`, the network doesn't have a gateway.
	NoIpv6Gateway pulumi.BoolPtrInput
	// STACKIT project ID to which the network is associated.
	ProjectId pulumi.StringInput
	// If set to `true`, the network is routed and therefore accessible from other networks.
	Routed pulumi.BoolPtrInput
}

func (NetworkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*networkArgs)(nil)).Elem()
}

type NetworkInput interface {
	pulumi.Input

	ToNetworkOutput() NetworkOutput
	ToNetworkOutputWithContext(ctx context.Context) NetworkOutput
}

func (*Network) ElementType() reflect.Type {
	return reflect.TypeOf((**Network)(nil)).Elem()
}

func (i *Network) ToNetworkOutput() NetworkOutput {
	return i.ToNetworkOutputWithContext(context.Background())
}

func (i *Network) ToNetworkOutputWithContext(ctx context.Context) NetworkOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkOutput)
}

// NetworkArrayInput is an input type that accepts NetworkArray and NetworkArrayOutput values.
// You can construct a concrete instance of `NetworkArrayInput` via:
//
//	NetworkArray{ NetworkArgs{...} }
type NetworkArrayInput interface {
	pulumi.Input

	ToNetworkArrayOutput() NetworkArrayOutput
	ToNetworkArrayOutputWithContext(context.Context) NetworkArrayOutput
}

type NetworkArray []NetworkInput

func (NetworkArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Network)(nil)).Elem()
}

func (i NetworkArray) ToNetworkArrayOutput() NetworkArrayOutput {
	return i.ToNetworkArrayOutputWithContext(context.Background())
}

func (i NetworkArray) ToNetworkArrayOutputWithContext(ctx context.Context) NetworkArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkArrayOutput)
}

// NetworkMapInput is an input type that accepts NetworkMap and NetworkMapOutput values.
// You can construct a concrete instance of `NetworkMapInput` via:
//
//	NetworkMap{ "key": NetworkArgs{...} }
type NetworkMapInput interface {
	pulumi.Input

	ToNetworkMapOutput() NetworkMapOutput
	ToNetworkMapOutputWithContext(context.Context) NetworkMapOutput
}

type NetworkMap map[string]NetworkInput

func (NetworkMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Network)(nil)).Elem()
}

func (i NetworkMap) ToNetworkMapOutput() NetworkMapOutput {
	return i.ToNetworkMapOutputWithContext(context.Background())
}

func (i NetworkMap) ToNetworkMapOutputWithContext(ctx context.Context) NetworkMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(NetworkMapOutput)
}

type NetworkOutput struct{ *pulumi.OutputState }

func (NetworkOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Network)(nil)).Elem()
}

func (o NetworkOutput) ToNetworkOutput() NetworkOutput {
	return o
}

func (o NetworkOutput) ToNetworkOutputWithContext(ctx context.Context) NetworkOutput {
	return o
}

// The IPv4 gateway of a network. If not specified, the first IP of the network will be assigned as the gateway.
func (o NetworkOutput) Ipv4Gateway() pulumi.StringOutput {
	return o.ApplyT(func(v *Network) pulumi.StringOutput { return v.Ipv4Gateway }).(pulumi.StringOutput)
}

// The IPv4 nameservers of the network.
func (o NetworkOutput) Ipv4Nameservers() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Network) pulumi.StringArrayOutput { return v.Ipv4Nameservers }).(pulumi.StringArrayOutput)
}

// The IPv4 prefix of the network (CIDR).
func (o NetworkOutput) Ipv4Prefix() pulumi.StringOutput {
	return o.ApplyT(func(v *Network) pulumi.StringOutput { return v.Ipv4Prefix }).(pulumi.StringOutput)
}

// The IPv4 prefix length of the network.
func (o NetworkOutput) Ipv4PrefixLength() pulumi.IntOutput {
	return o.ApplyT(func(v *Network) pulumi.IntOutput { return v.Ipv4PrefixLength }).(pulumi.IntOutput)
}

// The IPv4 prefixes of the network.
func (o NetworkOutput) Ipv4Prefixes() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Network) pulumi.StringArrayOutput { return v.Ipv4Prefixes }).(pulumi.StringArrayOutput)
}

// The IPv6 gateway of a network. If not specified, the first IP of the network will be assigned as the gateway.
func (o NetworkOutput) Ipv6Gateway() pulumi.StringOutput {
	return o.ApplyT(func(v *Network) pulumi.StringOutput { return v.Ipv6Gateway }).(pulumi.StringOutput)
}

// The IPv6 nameservers of the network.
func (o NetworkOutput) Ipv6Nameservers() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Network) pulumi.StringArrayOutput { return v.Ipv6Nameservers }).(pulumi.StringArrayOutput)
}

// The IPv6 prefix of the network (CIDR).
func (o NetworkOutput) Ipv6Prefix() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Network) pulumi.StringPtrOutput { return v.Ipv6Prefix }).(pulumi.StringPtrOutput)
}

// The IPv6 prefix length of the network.
func (o NetworkOutput) Ipv6PrefixLength() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Network) pulumi.IntPtrOutput { return v.Ipv6PrefixLength }).(pulumi.IntPtrOutput)
}

// The IPv6 prefixes of the network.
func (o NetworkOutput) Ipv6Prefixes() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Network) pulumi.StringArrayOutput { return v.Ipv6Prefixes }).(pulumi.StringArrayOutput)
}

// Labels are key-value string pairs which can be attached to a resource container
func (o NetworkOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Network) pulumi.StringMapOutput { return v.Labels }).(pulumi.StringMapOutput)
}

// The name of the network.
func (o NetworkOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Network) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// The nameservers of the network. This field is deprecated and will be removed soon, use `ipv4Nameservers` to configure the nameservers for IPv4.
//
// Deprecated: Use `ipv4Nameservers` to configure the nameservers for IPv4.
func (o NetworkOutput) Nameservers() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Network) pulumi.StringArrayOutput { return v.Nameservers }).(pulumi.StringArrayOutput)
}

// The network ID.
func (o NetworkOutput) NetworkId() pulumi.StringOutput {
	return o.ApplyT(func(v *Network) pulumi.StringOutput { return v.NetworkId }).(pulumi.StringOutput)
}

// If set to `true`, the network doesn't have a gateway.
func (o NetworkOutput) NoIpv4Gateway() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Network) pulumi.BoolPtrOutput { return v.NoIpv4Gateway }).(pulumi.BoolPtrOutput)
}

// If set to `true`, the network doesn't have a gateway.
func (o NetworkOutput) NoIpv6Gateway() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Network) pulumi.BoolPtrOutput { return v.NoIpv6Gateway }).(pulumi.BoolPtrOutput)
}

// The prefixes of the network. This field is deprecated and will be removed soon, use `ipv4Prefixes` to read the prefixes of the IPv4 networks.
//
// Deprecated: Use `ipv4Prefixes` to read the prefixes of the IPv4 networks.
func (o NetworkOutput) Prefixes() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Network) pulumi.StringArrayOutput { return v.Prefixes }).(pulumi.StringArrayOutput)
}

// STACKIT project ID to which the network is associated.
func (o NetworkOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v *Network) pulumi.StringOutput { return v.ProjectId }).(pulumi.StringOutput)
}

// The public IP of the network.
func (o NetworkOutput) PublicIp() pulumi.StringOutput {
	return o.ApplyT(func(v *Network) pulumi.StringOutput { return v.PublicIp }).(pulumi.StringOutput)
}

// If set to `true`, the network is routed and therefore accessible from other networks.
func (o NetworkOutput) Routed() pulumi.BoolOutput {
	return o.ApplyT(func(v *Network) pulumi.BoolOutput { return v.Routed }).(pulumi.BoolOutput)
}

type NetworkArrayOutput struct{ *pulumi.OutputState }

func (NetworkArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Network)(nil)).Elem()
}

func (o NetworkArrayOutput) ToNetworkArrayOutput() NetworkArrayOutput {
	return o
}

func (o NetworkArrayOutput) ToNetworkArrayOutputWithContext(ctx context.Context) NetworkArrayOutput {
	return o
}

func (o NetworkArrayOutput) Index(i pulumi.IntInput) NetworkOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Network {
		return vs[0].([]*Network)[vs[1].(int)]
	}).(NetworkOutput)
}

type NetworkMapOutput struct{ *pulumi.OutputState }

func (NetworkMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Network)(nil)).Elem()
}

func (o NetworkMapOutput) ToNetworkMapOutput() NetworkMapOutput {
	return o
}

func (o NetworkMapOutput) ToNetworkMapOutputWithContext(ctx context.Context) NetworkMapOutput {
	return o
}

func (o NetworkMapOutput) MapIndex(k pulumi.StringInput) NetworkOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Network {
		return vs[0].(map[string]*Network)[vs[1].(string)]
	}).(NetworkOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkInput)(nil)).Elem(), &Network{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkArrayInput)(nil)).Elem(), NetworkArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*NetworkMapInput)(nil)).Elem(), NetworkMap{})
	pulumi.RegisterOutputType(NetworkOutput{})
	pulumi.RegisterOutputType(NetworkArrayOutput{})
	pulumi.RegisterOutputType(NetworkMapOutput{})
}
