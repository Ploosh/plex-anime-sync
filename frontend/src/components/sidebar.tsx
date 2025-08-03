"use client"

import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  useSidebar
} from "@/components/ui/sidebar"
import { Home, Logs, Settings } from "lucide-react"
import { AccountDropdown } from "./account-dropdown"
import { ModeToggle } from "./mode-toggle"

const items = [
  {
    title: "Home",
    url: "#",
    icon: Home,
  },
  {
    title: "Integrations",
    url: "#",
    icon: Logs,
  },
  {
    title: "Settings",
    url: "#",
    icon: Settings,
  },
]

export const SIDEBAR_COOKIE_NAME = "sidebar_state"

export function AppSidebar() {
  const { open, openMobile } = useSidebar()
  return (
    <Sidebar collapsible="icon" >
      <SidebarContent>
        <SidebarGroup>
          <SidebarGroupLabel>Plex Sync</SidebarGroupLabel>
          <SidebarGroupContent>
            <SidebarMenu>
              {items.map((item) => (
                <SidebarMenuItem key={item.title}>
                  <SidebarMenuButton asChild>
                    <a href={item.url}>
                      <item.icon />
                      <span>{item.title}</span>
                    </a>
                  </SidebarMenuButton>
                </SidebarMenuItem>
              ))}
            </SidebarMenu>
          </SidebarGroupContent>
        </SidebarGroup>
        <SidebarGroup />
      </SidebarContent>
      <SidebarFooter>
        <div className="flex items-center justify-between">
          {(open || openMobile) && <AccountDropdown />}
          <ModeToggle />
        </div>
      </SidebarFooter>
    </Sidebar>
  )
}