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

// Observability instance resource schema. Must have a `region` specified in the provider configuration.
//
// ## Example Usage
type ObservabilityInstance struct {
	pulumi.CustomResourceState

	// The access control list for this instance. Each entry is an IP address range that is permitted to access, in CIDR notation.
	Acls pulumi.StringArrayOutput `pulumi:"acls"`
	// Alert configuration for the instance.
	AlertConfig ObservabilityInstanceAlertConfigPtrOutput `pulumi:"alertConfig"`
	// Specifies Alerting URL.
	AlertingUrl pulumi.StringOutput `pulumi:"alertingUrl"`
	// Specifies Observability instance dashboard URL.
	DashboardUrl pulumi.StringOutput `pulumi:"dashboardUrl"`
	// Specifies an initial Grafana admin password.
	GrafanaInitialAdminPassword pulumi.StringOutput `pulumi:"grafanaInitialAdminPassword"`
	// Specifies an initial Grafana admin username.
	GrafanaInitialAdminUser pulumi.StringOutput `pulumi:"grafanaInitialAdminUser"`
	// If true, anyone can access Grafana dashboards without logging in.
	GrafanaPublicReadAccess pulumi.BoolOutput `pulumi:"grafanaPublicReadAccess"`
	// Specifies Grafana URL.
	GrafanaUrl pulumi.StringOutput `pulumi:"grafanaUrl"`
	// The Observability instance ID.
	InstanceId pulumi.StringOutput `pulumi:"instanceId"`
	// Specifies if the instance can be updated.
	IsUpdatable     pulumi.BoolOutput   `pulumi:"isUpdatable"`
	JaegerTracesUrl pulumi.StringOutput `pulumi:"jaegerTracesUrl"`
	JaegerUiUrl     pulumi.StringOutput `pulumi:"jaegerUiUrl"`
	// Specifies URL for pushing logs.
	LogsPushUrl pulumi.StringOutput `pulumi:"logsPushUrl"`
	// Specifies Logs URL.
	LogsUrl pulumi.StringOutput `pulumi:"logsUrl"`
	// Specifies URL for pushing metrics.
	MetricsPushUrl pulumi.StringOutput `pulumi:"metricsPushUrl"`
	// Specifies for how many days the raw metrics are kept.
	MetricsRetentionDays pulumi.IntOutput `pulumi:"metricsRetentionDays"`
	// Specifies for how many days the 1h downsampled metrics are kept. must be less than the value of the 5m downsampling retention. Default is set to `0` (disabled).
	MetricsRetentionDays1hDownsampling pulumi.IntOutput `pulumi:"metricsRetentionDays1hDownsampling"`
	// Specifies for how many days the 5m downsampled metrics are kept. must be less than the value of the general retention. Default is set to `0` (disabled).
	MetricsRetentionDays5mDownsampling pulumi.IntOutput `pulumi:"metricsRetentionDays5mDownsampling"`
	// Specifies metrics URL.
	MetricsUrl pulumi.StringOutput `pulumi:"metricsUrl"`
	// The name of the Observability instance.
	Name          pulumi.StringOutput `pulumi:"name"`
	OtlpTracesUrl pulumi.StringOutput `pulumi:"otlpTracesUrl"`
	// Additional parameters.
	Parameters pulumi.StringMapOutput `pulumi:"parameters"`
	// The Observability plan ID.
	PlanId pulumi.StringOutput `pulumi:"planId"`
	// Specifies the Observability plan. E.g. `Observability-Monitoring-Medium-EU01`.
	PlanName pulumi.StringOutput `pulumi:"planName"`
	// STACKIT project ID to which the instance is associated.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// Specifies Targets URL.
	TargetsUrl     pulumi.StringOutput `pulumi:"targetsUrl"`
	ZipkinSpansUrl pulumi.StringOutput `pulumi:"zipkinSpansUrl"`
}

// NewObservabilityInstance registers a new resource with the given unique name, arguments, and options.
func NewObservabilityInstance(ctx *pulumi.Context,
	name string, args *ObservabilityInstanceArgs, opts ...pulumi.ResourceOption) (*ObservabilityInstance, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PlanName == nil {
		return nil, errors.New("invalid value for required argument 'PlanName'")
	}
	if args.ProjectId == nil {
		return nil, errors.New("invalid value for required argument 'ProjectId'")
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"grafanaInitialAdminPassword",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ObservabilityInstance
	err := ctx.RegisterResource("stackit:index/observabilityInstance:ObservabilityInstance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetObservabilityInstance gets an existing ObservabilityInstance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetObservabilityInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ObservabilityInstanceState, opts ...pulumi.ResourceOption) (*ObservabilityInstance, error) {
	var resource ObservabilityInstance
	err := ctx.ReadResource("stackit:index/observabilityInstance:ObservabilityInstance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ObservabilityInstance resources.
type observabilityInstanceState struct {
	// The access control list for this instance. Each entry is an IP address range that is permitted to access, in CIDR notation.
	Acls []string `pulumi:"acls"`
	// Alert configuration for the instance.
	AlertConfig *ObservabilityInstanceAlertConfig `pulumi:"alertConfig"`
	// Specifies Alerting URL.
	AlertingUrl *string `pulumi:"alertingUrl"`
	// Specifies Observability instance dashboard URL.
	DashboardUrl *string `pulumi:"dashboardUrl"`
	// Specifies an initial Grafana admin password.
	GrafanaInitialAdminPassword *string `pulumi:"grafanaInitialAdminPassword"`
	// Specifies an initial Grafana admin username.
	GrafanaInitialAdminUser *string `pulumi:"grafanaInitialAdminUser"`
	// If true, anyone can access Grafana dashboards without logging in.
	GrafanaPublicReadAccess *bool `pulumi:"grafanaPublicReadAccess"`
	// Specifies Grafana URL.
	GrafanaUrl *string `pulumi:"grafanaUrl"`
	// The Observability instance ID.
	InstanceId *string `pulumi:"instanceId"`
	// Specifies if the instance can be updated.
	IsUpdatable     *bool   `pulumi:"isUpdatable"`
	JaegerTracesUrl *string `pulumi:"jaegerTracesUrl"`
	JaegerUiUrl     *string `pulumi:"jaegerUiUrl"`
	// Specifies URL for pushing logs.
	LogsPushUrl *string `pulumi:"logsPushUrl"`
	// Specifies Logs URL.
	LogsUrl *string `pulumi:"logsUrl"`
	// Specifies URL for pushing metrics.
	MetricsPushUrl *string `pulumi:"metricsPushUrl"`
	// Specifies for how many days the raw metrics are kept.
	MetricsRetentionDays *int `pulumi:"metricsRetentionDays"`
	// Specifies for how many days the 1h downsampled metrics are kept. must be less than the value of the 5m downsampling retention. Default is set to `0` (disabled).
	MetricsRetentionDays1hDownsampling *int `pulumi:"metricsRetentionDays1hDownsampling"`
	// Specifies for how many days the 5m downsampled metrics are kept. must be less than the value of the general retention. Default is set to `0` (disabled).
	MetricsRetentionDays5mDownsampling *int `pulumi:"metricsRetentionDays5mDownsampling"`
	// Specifies metrics URL.
	MetricsUrl *string `pulumi:"metricsUrl"`
	// The name of the Observability instance.
	Name          *string `pulumi:"name"`
	OtlpTracesUrl *string `pulumi:"otlpTracesUrl"`
	// Additional parameters.
	Parameters map[string]string `pulumi:"parameters"`
	// The Observability plan ID.
	PlanId *string `pulumi:"planId"`
	// Specifies the Observability plan. E.g. `Observability-Monitoring-Medium-EU01`.
	PlanName *string `pulumi:"planName"`
	// STACKIT project ID to which the instance is associated.
	ProjectId *string `pulumi:"projectId"`
	// Specifies Targets URL.
	TargetsUrl     *string `pulumi:"targetsUrl"`
	ZipkinSpansUrl *string `pulumi:"zipkinSpansUrl"`
}

type ObservabilityInstanceState struct {
	// The access control list for this instance. Each entry is an IP address range that is permitted to access, in CIDR notation.
	Acls pulumi.StringArrayInput
	// Alert configuration for the instance.
	AlertConfig ObservabilityInstanceAlertConfigPtrInput
	// Specifies Alerting URL.
	AlertingUrl pulumi.StringPtrInput
	// Specifies Observability instance dashboard URL.
	DashboardUrl pulumi.StringPtrInput
	// Specifies an initial Grafana admin password.
	GrafanaInitialAdminPassword pulumi.StringPtrInput
	// Specifies an initial Grafana admin username.
	GrafanaInitialAdminUser pulumi.StringPtrInput
	// If true, anyone can access Grafana dashboards without logging in.
	GrafanaPublicReadAccess pulumi.BoolPtrInput
	// Specifies Grafana URL.
	GrafanaUrl pulumi.StringPtrInput
	// The Observability instance ID.
	InstanceId pulumi.StringPtrInput
	// Specifies if the instance can be updated.
	IsUpdatable     pulumi.BoolPtrInput
	JaegerTracesUrl pulumi.StringPtrInput
	JaegerUiUrl     pulumi.StringPtrInput
	// Specifies URL for pushing logs.
	LogsPushUrl pulumi.StringPtrInput
	// Specifies Logs URL.
	LogsUrl pulumi.StringPtrInput
	// Specifies URL for pushing metrics.
	MetricsPushUrl pulumi.StringPtrInput
	// Specifies for how many days the raw metrics are kept.
	MetricsRetentionDays pulumi.IntPtrInput
	// Specifies for how many days the 1h downsampled metrics are kept. must be less than the value of the 5m downsampling retention. Default is set to `0` (disabled).
	MetricsRetentionDays1hDownsampling pulumi.IntPtrInput
	// Specifies for how many days the 5m downsampled metrics are kept. must be less than the value of the general retention. Default is set to `0` (disabled).
	MetricsRetentionDays5mDownsampling pulumi.IntPtrInput
	// Specifies metrics URL.
	MetricsUrl pulumi.StringPtrInput
	// The name of the Observability instance.
	Name          pulumi.StringPtrInput
	OtlpTracesUrl pulumi.StringPtrInput
	// Additional parameters.
	Parameters pulumi.StringMapInput
	// The Observability plan ID.
	PlanId pulumi.StringPtrInput
	// Specifies the Observability plan. E.g. `Observability-Monitoring-Medium-EU01`.
	PlanName pulumi.StringPtrInput
	// STACKIT project ID to which the instance is associated.
	ProjectId pulumi.StringPtrInput
	// Specifies Targets URL.
	TargetsUrl     pulumi.StringPtrInput
	ZipkinSpansUrl pulumi.StringPtrInput
}

func (ObservabilityInstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*observabilityInstanceState)(nil)).Elem()
}

type observabilityInstanceArgs struct {
	// The access control list for this instance. Each entry is an IP address range that is permitted to access, in CIDR notation.
	Acls []string `pulumi:"acls"`
	// Alert configuration for the instance.
	AlertConfig *ObservabilityInstanceAlertConfig `pulumi:"alertConfig"`
	// Specifies for how many days the raw metrics are kept.
	MetricsRetentionDays *int `pulumi:"metricsRetentionDays"`
	// Specifies for how many days the 1h downsampled metrics are kept. must be less than the value of the 5m downsampling retention. Default is set to `0` (disabled).
	MetricsRetentionDays1hDownsampling *int `pulumi:"metricsRetentionDays1hDownsampling"`
	// Specifies for how many days the 5m downsampled metrics are kept. must be less than the value of the general retention. Default is set to `0` (disabled).
	MetricsRetentionDays5mDownsampling *int `pulumi:"metricsRetentionDays5mDownsampling"`
	// The name of the Observability instance.
	Name *string `pulumi:"name"`
	// Additional parameters.
	Parameters map[string]string `pulumi:"parameters"`
	// Specifies the Observability plan. E.g. `Observability-Monitoring-Medium-EU01`.
	PlanName string `pulumi:"planName"`
	// STACKIT project ID to which the instance is associated.
	ProjectId string `pulumi:"projectId"`
}

// The set of arguments for constructing a ObservabilityInstance resource.
type ObservabilityInstanceArgs struct {
	// The access control list for this instance. Each entry is an IP address range that is permitted to access, in CIDR notation.
	Acls pulumi.StringArrayInput
	// Alert configuration for the instance.
	AlertConfig ObservabilityInstanceAlertConfigPtrInput
	// Specifies for how many days the raw metrics are kept.
	MetricsRetentionDays pulumi.IntPtrInput
	// Specifies for how many days the 1h downsampled metrics are kept. must be less than the value of the 5m downsampling retention. Default is set to `0` (disabled).
	MetricsRetentionDays1hDownsampling pulumi.IntPtrInput
	// Specifies for how many days the 5m downsampled metrics are kept. must be less than the value of the general retention. Default is set to `0` (disabled).
	MetricsRetentionDays5mDownsampling pulumi.IntPtrInput
	// The name of the Observability instance.
	Name pulumi.StringPtrInput
	// Additional parameters.
	Parameters pulumi.StringMapInput
	// Specifies the Observability plan. E.g. `Observability-Monitoring-Medium-EU01`.
	PlanName pulumi.StringInput
	// STACKIT project ID to which the instance is associated.
	ProjectId pulumi.StringInput
}

func (ObservabilityInstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*observabilityInstanceArgs)(nil)).Elem()
}

type ObservabilityInstanceInput interface {
	pulumi.Input

	ToObservabilityInstanceOutput() ObservabilityInstanceOutput
	ToObservabilityInstanceOutputWithContext(ctx context.Context) ObservabilityInstanceOutput
}

func (*ObservabilityInstance) ElementType() reflect.Type {
	return reflect.TypeOf((**ObservabilityInstance)(nil)).Elem()
}

func (i *ObservabilityInstance) ToObservabilityInstanceOutput() ObservabilityInstanceOutput {
	return i.ToObservabilityInstanceOutputWithContext(context.Background())
}

func (i *ObservabilityInstance) ToObservabilityInstanceOutputWithContext(ctx context.Context) ObservabilityInstanceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ObservabilityInstanceOutput)
}

// ObservabilityInstanceArrayInput is an input type that accepts ObservabilityInstanceArray and ObservabilityInstanceArrayOutput values.
// You can construct a concrete instance of `ObservabilityInstanceArrayInput` via:
//
//	ObservabilityInstanceArray{ ObservabilityInstanceArgs{...} }
type ObservabilityInstanceArrayInput interface {
	pulumi.Input

	ToObservabilityInstanceArrayOutput() ObservabilityInstanceArrayOutput
	ToObservabilityInstanceArrayOutputWithContext(context.Context) ObservabilityInstanceArrayOutput
}

type ObservabilityInstanceArray []ObservabilityInstanceInput

func (ObservabilityInstanceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ObservabilityInstance)(nil)).Elem()
}

func (i ObservabilityInstanceArray) ToObservabilityInstanceArrayOutput() ObservabilityInstanceArrayOutput {
	return i.ToObservabilityInstanceArrayOutputWithContext(context.Background())
}

func (i ObservabilityInstanceArray) ToObservabilityInstanceArrayOutputWithContext(ctx context.Context) ObservabilityInstanceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ObservabilityInstanceArrayOutput)
}

// ObservabilityInstanceMapInput is an input type that accepts ObservabilityInstanceMap and ObservabilityInstanceMapOutput values.
// You can construct a concrete instance of `ObservabilityInstanceMapInput` via:
//
//	ObservabilityInstanceMap{ "key": ObservabilityInstanceArgs{...} }
type ObservabilityInstanceMapInput interface {
	pulumi.Input

	ToObservabilityInstanceMapOutput() ObservabilityInstanceMapOutput
	ToObservabilityInstanceMapOutputWithContext(context.Context) ObservabilityInstanceMapOutput
}

type ObservabilityInstanceMap map[string]ObservabilityInstanceInput

func (ObservabilityInstanceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ObservabilityInstance)(nil)).Elem()
}

func (i ObservabilityInstanceMap) ToObservabilityInstanceMapOutput() ObservabilityInstanceMapOutput {
	return i.ToObservabilityInstanceMapOutputWithContext(context.Background())
}

func (i ObservabilityInstanceMap) ToObservabilityInstanceMapOutputWithContext(ctx context.Context) ObservabilityInstanceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ObservabilityInstanceMapOutput)
}

type ObservabilityInstanceOutput struct{ *pulumi.OutputState }

func (ObservabilityInstanceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ObservabilityInstance)(nil)).Elem()
}

func (o ObservabilityInstanceOutput) ToObservabilityInstanceOutput() ObservabilityInstanceOutput {
	return o
}

func (o ObservabilityInstanceOutput) ToObservabilityInstanceOutputWithContext(ctx context.Context) ObservabilityInstanceOutput {
	return o
}

// The access control list for this instance. Each entry is an IP address range that is permitted to access, in CIDR notation.
func (o ObservabilityInstanceOutput) Acls() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringArrayOutput { return v.Acls }).(pulumi.StringArrayOutput)
}

// Alert configuration for the instance.
func (o ObservabilityInstanceOutput) AlertConfig() ObservabilityInstanceAlertConfigPtrOutput {
	return o.ApplyT(func(v *ObservabilityInstance) ObservabilityInstanceAlertConfigPtrOutput { return v.AlertConfig }).(ObservabilityInstanceAlertConfigPtrOutput)
}

// Specifies Alerting URL.
func (o ObservabilityInstanceOutput) AlertingUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.AlertingUrl }).(pulumi.StringOutput)
}

// Specifies Observability instance dashboard URL.
func (o ObservabilityInstanceOutput) DashboardUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.DashboardUrl }).(pulumi.StringOutput)
}

// Specifies an initial Grafana admin password.
func (o ObservabilityInstanceOutput) GrafanaInitialAdminPassword() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.GrafanaInitialAdminPassword }).(pulumi.StringOutput)
}

// Specifies an initial Grafana admin username.
func (o ObservabilityInstanceOutput) GrafanaInitialAdminUser() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.GrafanaInitialAdminUser }).(pulumi.StringOutput)
}

// If true, anyone can access Grafana dashboards without logging in.
func (o ObservabilityInstanceOutput) GrafanaPublicReadAccess() pulumi.BoolOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.BoolOutput { return v.GrafanaPublicReadAccess }).(pulumi.BoolOutput)
}

// Specifies Grafana URL.
func (o ObservabilityInstanceOutput) GrafanaUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.GrafanaUrl }).(pulumi.StringOutput)
}

// The Observability instance ID.
func (o ObservabilityInstanceOutput) InstanceId() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.InstanceId }).(pulumi.StringOutput)
}

// Specifies if the instance can be updated.
func (o ObservabilityInstanceOutput) IsUpdatable() pulumi.BoolOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.BoolOutput { return v.IsUpdatable }).(pulumi.BoolOutput)
}

func (o ObservabilityInstanceOutput) JaegerTracesUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.JaegerTracesUrl }).(pulumi.StringOutput)
}

func (o ObservabilityInstanceOutput) JaegerUiUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.JaegerUiUrl }).(pulumi.StringOutput)
}

// Specifies URL for pushing logs.
func (o ObservabilityInstanceOutput) LogsPushUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.LogsPushUrl }).(pulumi.StringOutput)
}

// Specifies Logs URL.
func (o ObservabilityInstanceOutput) LogsUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.LogsUrl }).(pulumi.StringOutput)
}

// Specifies URL for pushing metrics.
func (o ObservabilityInstanceOutput) MetricsPushUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.MetricsPushUrl }).(pulumi.StringOutput)
}

// Specifies for how many days the raw metrics are kept.
func (o ObservabilityInstanceOutput) MetricsRetentionDays() pulumi.IntOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.IntOutput { return v.MetricsRetentionDays }).(pulumi.IntOutput)
}

// Specifies for how many days the 1h downsampled metrics are kept. must be less than the value of the 5m downsampling retention. Default is set to `0` (disabled).
func (o ObservabilityInstanceOutput) MetricsRetentionDays1hDownsampling() pulumi.IntOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.IntOutput { return v.MetricsRetentionDays1hDownsampling }).(pulumi.IntOutput)
}

// Specifies for how many days the 5m downsampled metrics are kept. must be less than the value of the general retention. Default is set to `0` (disabled).
func (o ObservabilityInstanceOutput) MetricsRetentionDays5mDownsampling() pulumi.IntOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.IntOutput { return v.MetricsRetentionDays5mDownsampling }).(pulumi.IntOutput)
}

// Specifies metrics URL.
func (o ObservabilityInstanceOutput) MetricsUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.MetricsUrl }).(pulumi.StringOutput)
}

// The name of the Observability instance.
func (o ObservabilityInstanceOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o ObservabilityInstanceOutput) OtlpTracesUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.OtlpTracesUrl }).(pulumi.StringOutput)
}

// Additional parameters.
func (o ObservabilityInstanceOutput) Parameters() pulumi.StringMapOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringMapOutput { return v.Parameters }).(pulumi.StringMapOutput)
}

// The Observability plan ID.
func (o ObservabilityInstanceOutput) PlanId() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.PlanId }).(pulumi.StringOutput)
}

// Specifies the Observability plan. E.g. `Observability-Monitoring-Medium-EU01`.
func (o ObservabilityInstanceOutput) PlanName() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.PlanName }).(pulumi.StringOutput)
}

// STACKIT project ID to which the instance is associated.
func (o ObservabilityInstanceOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.ProjectId }).(pulumi.StringOutput)
}

// Specifies Targets URL.
func (o ObservabilityInstanceOutput) TargetsUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.TargetsUrl }).(pulumi.StringOutput)
}

func (o ObservabilityInstanceOutput) ZipkinSpansUrl() pulumi.StringOutput {
	return o.ApplyT(func(v *ObservabilityInstance) pulumi.StringOutput { return v.ZipkinSpansUrl }).(pulumi.StringOutput)
}

type ObservabilityInstanceArrayOutput struct{ *pulumi.OutputState }

func (ObservabilityInstanceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ObservabilityInstance)(nil)).Elem()
}

func (o ObservabilityInstanceArrayOutput) ToObservabilityInstanceArrayOutput() ObservabilityInstanceArrayOutput {
	return o
}

func (o ObservabilityInstanceArrayOutput) ToObservabilityInstanceArrayOutputWithContext(ctx context.Context) ObservabilityInstanceArrayOutput {
	return o
}

func (o ObservabilityInstanceArrayOutput) Index(i pulumi.IntInput) ObservabilityInstanceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ObservabilityInstance {
		return vs[0].([]*ObservabilityInstance)[vs[1].(int)]
	}).(ObservabilityInstanceOutput)
}

type ObservabilityInstanceMapOutput struct{ *pulumi.OutputState }

func (ObservabilityInstanceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ObservabilityInstance)(nil)).Elem()
}

func (o ObservabilityInstanceMapOutput) ToObservabilityInstanceMapOutput() ObservabilityInstanceMapOutput {
	return o
}

func (o ObservabilityInstanceMapOutput) ToObservabilityInstanceMapOutputWithContext(ctx context.Context) ObservabilityInstanceMapOutput {
	return o
}

func (o ObservabilityInstanceMapOutput) MapIndex(k pulumi.StringInput) ObservabilityInstanceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ObservabilityInstance {
		return vs[0].(map[string]*ObservabilityInstance)[vs[1].(string)]
	}).(ObservabilityInstanceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ObservabilityInstanceInput)(nil)).Elem(), &ObservabilityInstance{})
	pulumi.RegisterInputType(reflect.TypeOf((*ObservabilityInstanceArrayInput)(nil)).Elem(), ObservabilityInstanceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ObservabilityInstanceMapInput)(nil)).Elem(), ObservabilityInstanceMap{})
	pulumi.RegisterOutputType(ObservabilityInstanceOutput{})
	pulumi.RegisterOutputType(ObservabilityInstanceArrayOutput{})
	pulumi.RegisterOutputType(ObservabilityInstanceMapOutput{})
}
