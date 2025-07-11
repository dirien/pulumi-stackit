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

// Key pair resource schema. Must have a `region` specified in the provider configuration. Allows uploading an SSH public key to be used for server authentication.
type KeyPair struct {
	pulumi.CustomResourceState

	// The fingerprint of the public SSH key.
	Fingerprint pulumi.StringOutput `pulumi:"fingerprint"`
	// Labels are key-value string pairs which can be attached to a resource container.
	Labels pulumi.StringMapOutput `pulumi:"labels"`
	// The name of the SSH key pair.
	Name pulumi.StringOutput `pulumi:"name"`
	// A string representation of the public SSH key. E.g., `ssh-rsa <key_data>` or `ssh-ed25519 <key-data>`.
	PublicKey pulumi.StringOutput `pulumi:"publicKey"`
}

// NewKeyPair registers a new resource with the given unique name, arguments, and options.
func NewKeyPair(ctx *pulumi.Context,
	name string, args *KeyPairArgs, opts ...pulumi.ResourceOption) (*KeyPair, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PublicKey == nil {
		return nil, errors.New("invalid value for required argument 'PublicKey'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource KeyPair
	err := ctx.RegisterResource("stackit:index/keyPair:KeyPair", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetKeyPair gets an existing KeyPair resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetKeyPair(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *KeyPairState, opts ...pulumi.ResourceOption) (*KeyPair, error) {
	var resource KeyPair
	err := ctx.ReadResource("stackit:index/keyPair:KeyPair", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering KeyPair resources.
type keyPairState struct {
	// The fingerprint of the public SSH key.
	Fingerprint *string `pulumi:"fingerprint"`
	// Labels are key-value string pairs which can be attached to a resource container.
	Labels map[string]string `pulumi:"labels"`
	// The name of the SSH key pair.
	Name *string `pulumi:"name"`
	// A string representation of the public SSH key. E.g., `ssh-rsa <key_data>` or `ssh-ed25519 <key-data>`.
	PublicKey *string `pulumi:"publicKey"`
}

type KeyPairState struct {
	// The fingerprint of the public SSH key.
	Fingerprint pulumi.StringPtrInput
	// Labels are key-value string pairs which can be attached to a resource container.
	Labels pulumi.StringMapInput
	// The name of the SSH key pair.
	Name pulumi.StringPtrInput
	// A string representation of the public SSH key. E.g., `ssh-rsa <key_data>` or `ssh-ed25519 <key-data>`.
	PublicKey pulumi.StringPtrInput
}

func (KeyPairState) ElementType() reflect.Type {
	return reflect.TypeOf((*keyPairState)(nil)).Elem()
}

type keyPairArgs struct {
	// Labels are key-value string pairs which can be attached to a resource container.
	Labels map[string]string `pulumi:"labels"`
	// The name of the SSH key pair.
	Name *string `pulumi:"name"`
	// A string representation of the public SSH key. E.g., `ssh-rsa <key_data>` or `ssh-ed25519 <key-data>`.
	PublicKey string `pulumi:"publicKey"`
}

// The set of arguments for constructing a KeyPair resource.
type KeyPairArgs struct {
	// Labels are key-value string pairs which can be attached to a resource container.
	Labels pulumi.StringMapInput
	// The name of the SSH key pair.
	Name pulumi.StringPtrInput
	// A string representation of the public SSH key. E.g., `ssh-rsa <key_data>` or `ssh-ed25519 <key-data>`.
	PublicKey pulumi.StringInput
}

func (KeyPairArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*keyPairArgs)(nil)).Elem()
}

type KeyPairInput interface {
	pulumi.Input

	ToKeyPairOutput() KeyPairOutput
	ToKeyPairOutputWithContext(ctx context.Context) KeyPairOutput
}

func (*KeyPair) ElementType() reflect.Type {
	return reflect.TypeOf((**KeyPair)(nil)).Elem()
}

func (i *KeyPair) ToKeyPairOutput() KeyPairOutput {
	return i.ToKeyPairOutputWithContext(context.Background())
}

func (i *KeyPair) ToKeyPairOutputWithContext(ctx context.Context) KeyPairOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KeyPairOutput)
}

// KeyPairArrayInput is an input type that accepts KeyPairArray and KeyPairArrayOutput values.
// You can construct a concrete instance of `KeyPairArrayInput` via:
//
//	KeyPairArray{ KeyPairArgs{...} }
type KeyPairArrayInput interface {
	pulumi.Input

	ToKeyPairArrayOutput() KeyPairArrayOutput
	ToKeyPairArrayOutputWithContext(context.Context) KeyPairArrayOutput
}

type KeyPairArray []KeyPairInput

func (KeyPairArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*KeyPair)(nil)).Elem()
}

func (i KeyPairArray) ToKeyPairArrayOutput() KeyPairArrayOutput {
	return i.ToKeyPairArrayOutputWithContext(context.Background())
}

func (i KeyPairArray) ToKeyPairArrayOutputWithContext(ctx context.Context) KeyPairArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KeyPairArrayOutput)
}

// KeyPairMapInput is an input type that accepts KeyPairMap and KeyPairMapOutput values.
// You can construct a concrete instance of `KeyPairMapInput` via:
//
//	KeyPairMap{ "key": KeyPairArgs{...} }
type KeyPairMapInput interface {
	pulumi.Input

	ToKeyPairMapOutput() KeyPairMapOutput
	ToKeyPairMapOutputWithContext(context.Context) KeyPairMapOutput
}

type KeyPairMap map[string]KeyPairInput

func (KeyPairMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*KeyPair)(nil)).Elem()
}

func (i KeyPairMap) ToKeyPairMapOutput() KeyPairMapOutput {
	return i.ToKeyPairMapOutputWithContext(context.Background())
}

func (i KeyPairMap) ToKeyPairMapOutputWithContext(ctx context.Context) KeyPairMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KeyPairMapOutput)
}

type KeyPairOutput struct{ *pulumi.OutputState }

func (KeyPairOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**KeyPair)(nil)).Elem()
}

func (o KeyPairOutput) ToKeyPairOutput() KeyPairOutput {
	return o
}

func (o KeyPairOutput) ToKeyPairOutputWithContext(ctx context.Context) KeyPairOutput {
	return o
}

// The fingerprint of the public SSH key.
func (o KeyPairOutput) Fingerprint() pulumi.StringOutput {
	return o.ApplyT(func(v *KeyPair) pulumi.StringOutput { return v.Fingerprint }).(pulumi.StringOutput)
}

// Labels are key-value string pairs which can be attached to a resource container.
func (o KeyPairOutput) Labels() pulumi.StringMapOutput {
	return o.ApplyT(func(v *KeyPair) pulumi.StringMapOutput { return v.Labels }).(pulumi.StringMapOutput)
}

// The name of the SSH key pair.
func (o KeyPairOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *KeyPair) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// A string representation of the public SSH key. E.g., `ssh-rsa <key_data>` or `ssh-ed25519 <key-data>`.
func (o KeyPairOutput) PublicKey() pulumi.StringOutput {
	return o.ApplyT(func(v *KeyPair) pulumi.StringOutput { return v.PublicKey }).(pulumi.StringOutput)
}

type KeyPairArrayOutput struct{ *pulumi.OutputState }

func (KeyPairArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*KeyPair)(nil)).Elem()
}

func (o KeyPairArrayOutput) ToKeyPairArrayOutput() KeyPairArrayOutput {
	return o
}

func (o KeyPairArrayOutput) ToKeyPairArrayOutputWithContext(ctx context.Context) KeyPairArrayOutput {
	return o
}

func (o KeyPairArrayOutput) Index(i pulumi.IntInput) KeyPairOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *KeyPair {
		return vs[0].([]*KeyPair)[vs[1].(int)]
	}).(KeyPairOutput)
}

type KeyPairMapOutput struct{ *pulumi.OutputState }

func (KeyPairMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*KeyPair)(nil)).Elem()
}

func (o KeyPairMapOutput) ToKeyPairMapOutput() KeyPairMapOutput {
	return o
}

func (o KeyPairMapOutput) ToKeyPairMapOutputWithContext(ctx context.Context) KeyPairMapOutput {
	return o
}

func (o KeyPairMapOutput) MapIndex(k pulumi.StringInput) KeyPairOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *KeyPair {
		return vs[0].(map[string]*KeyPair)[vs[1].(string)]
	}).(KeyPairOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*KeyPairInput)(nil)).Elem(), &KeyPair{})
	pulumi.RegisterInputType(reflect.TypeOf((*KeyPairArrayInput)(nil)).Elem(), KeyPairArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*KeyPairMapInput)(nil)).Elem(), KeyPairMap{})
	pulumi.RegisterOutputType(KeyPairOutput{})
	pulumi.RegisterOutputType(KeyPairArrayOutput{})
	pulumi.RegisterOutputType(KeyPairMapOutput{})
}
