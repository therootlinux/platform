package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
)

var free bool

var deployCmd = &cobra.Command{
	Use:   "deploy",
	Short: "Deploy a cloud instance",
	Run: func(cmd *cobra.Command, args []string) {
		if free {
			fmt.Println("✓ Free instance deployed!")
			fmt.Println("🌐 Access it at: https://vm123.mycloud.com")
		} else {
			fmt.Println("🚀 Deploying paid instance...")
			
		}
	},
}

func init() {
	deployCmd.Flags().BoolVar(&free, "free", false, "Deploy a free instance")
	rootCmd.AddCommand(deployCmd)
}
