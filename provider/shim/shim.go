package shim

import (
	"github.com/dirien/pulumi-stackit/provider/pkg/version"
	"github.com/hashicorp/terraform-plugin-framework/provider"
	"github.com/stackitcloud/terraform-provider-stackit/stackit"
)

func NewProvider() provider.Provider {
	p := stackit.New(version.Version)
	return p()
}
