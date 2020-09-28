"""Metadata for protocol version 578"""
from enum import Enum

version = 578
game_version = "1.15.2"

packet_id_lookup = {
    "handshake": 0x00,
    "legacy_server_list_ping": 0xfe,
    "response": 0x00,
    "pong": 0x01,
    "request": 0x00,
    "ping": 0x01,
    "disconnect_login": 0x00,
    "encryption_request": 0x01,
    "login_success": 0x02,
    "set_compression": 0x03,
    "login_plugin_request": 0x04,
    "login_start": 0x00,
    "encryption_response": 0x01,
    "login_plugin_response": 0x02,
    "spawn_entity": 0x00,
    "spawn_experience_orb": 0x01,
    "spawn_weather_entity": 0x02,
    "spawn_living_entity": 0x03,
    "spawn_painting": 0x04,
    "spawn_player": 0x05,
    "entity_animation_clientbound": 0x06,
    "statistics": 0x07,
    "acknowledge_player_digging": 0x08,
    "block_break_animation": 0x09,
    "block_entity_data": 0x0a,
    "block_action": 0x0b,
    "block_change": 0x0c,
    "boss_bar": 0x0d,
    "server_difficulty": 0x0e,
    "chat_message_clientbound": 0x0f,
    "multi_block_change": 0x10,
    "tab_complete_clientbound": 0x11,
    "declare_commands": 0x12,
    "window_confirmation_clientbound": 0x13,
    "close_window_clientbound": 0x14,
    "window_items": 0x15,
    "window_property": 0x16,
    "set_slot": 0x17,
    "set_cooldown": 0x18,
    "plugin_message_clientbound": 0x19,
    "named_sound_effect": 0x1a,
    "disconnect_play": 0x1b,
    "entity_status": 0x1c,
    "explosion": 0x1d,
    "unload_chunk": 0x1e,
    "change_game_state": 0x1f,
    "open_horse_window": 0x20,
    "keep_alive_clientbound": 0x21,
    "chunk_data": 0x22,
    "effect": 0x23,
    "particle": 0x24,
    "update_light": 0x25,
    "join_game": 0x26,
    "map_data": 0x27,
    "trade_list": 0x28,
    "entity_position": 0x29,
    "entity_position_and_rotation": 0x2a,
    "entity_rotation": 0x2b,
    "entity_movement": 0x2c,
    "vehicle_move_clientbound": 0x2d,
    "open_book": 0x2e,
    "open_window": 0x2f,
    "open_sign_editor": 0x30,
    "craft_recipe_response": 0x31,
    "player_abilities_clientbound": 0x32,
    "combat_event": 0x33,
    "player_info": 0x34,
    "face_player": 0x35,
    "player_position_and_look_clientbound": 0x36,
    "unlock_recipes": 0x37,
    "destroy_entities": 0x38,
    "remove_entity_effect": 0x39,
    "resource_pack_send": 0x3a,
    "respawn": 0x3b,
    "entity_head_look": 0x3c,
    "select_advancement_tab": 0x3d,
    "world_border": 0x3e,
    "camera": 0x3f,
    "held_item_change_clientbound": 0x40,
    "update_view_position": 0x41,
    "update_view_distance": 0x42,
    "display_scoreboard": 0x43,
    "entity_metadata": 0x44,
    "attach_entity": 0x45,
    "entity_velocity": 0x46,
    "entity_equipment": 0x47,
    "set_experience": 0x48,
    "update_health": 0x49,
    "scoreboard_objective": 0x4a,
    "set_passengers": 0x4b,
    "teams": 0x4c,
    "update_score": 0x4d,
    "spawn_position": 0x4e,
    "time_update": 0x4f,
    "title": 0x50,
    "entity_sound_effect": 0x51,
    "sound_effect": 0x52,
    "stop_sound": 0x53,
    "player_list_header_and_footer": 0x54,
    "nbt_query_response": 0x55,
    "collect_item": 0x56,
    "entity_teleport": 0x57,
    "advancements": 0x58,
    "entity_properties": 0x59,
    "entity_effect": 0x5a,
    "declare_recipes": 0x5b,
    "tags": 0x5c,
    "teleport_confirm": 0x00,
    "query_block_nbt": 0x01,
    "set_difficulty": 0x02,
    "chat_message_serverbound": 0x03,
    "client_status": 0x04,
    "client_settings": 0x05,
    "tab_complete_serverbound": 0x06,
    "window_confirmation_serverbound": 0x07,
    "click_window_button": 0x08,
    "click_window": 0x09,
    "close_window_serverbound": 0x0a,
    "plugin_message_serverbound": 0x0b,
    "edit_book": 0x0c,
    "entity_nbt_request": 0x0d,
    "interact_entity": 0x0e,
    "keep_alive_serverbound": 0x0f,
    "lock_difficulty": 0x10,
    "player_position": 0x11,
    "player_position_and_rotation_serverbound": 0x12,
    "player_rotation": 0x13,
    "player_movement": 0x14,
    "vehicle_move_serverbound": 0x15,
    "steer_boat": 0x16,
    "pick_item": 0x17,
    "craft_recipe_request": 0x18,
    "player_abilities_serverbound": 0x19,
    "player_digging": 0x1a,
    "entity_action": 0x1b,
    "steer_vehicle": 0x1c,
    "recipe_book_data": 0x1d,
    "name_item": 0x1e,
    "resource_pack_status": 0x1f,
    "advancement_tab": 0x20,
    "select_trade": 0x21,
    "set_beacon_effect": 0x22,
    "held_item_change_serverbound": 0x23,
    "update_command_block": 0x24,
    "update_command_block_minecart": 0x25,
    "creative_inventory_action": 0x26,
    "update_jigsaw_block": 0x27,
    "update_structure_block": 0x28,
    "update_sign": 0x29,
    "animation_serverbound": 0x2a,
    "spectate": 0x2b,
    "player_block_placement": 0x2c,
    "use_item": 0x2d
}

packet_id_enum = Enum("Packet IDs", packet_id_lookup)

