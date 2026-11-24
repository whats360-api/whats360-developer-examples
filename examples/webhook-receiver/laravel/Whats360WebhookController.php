<?php
// Laravel controller sketch. NOT executed (no PHP/Laravel in the build environment).
// 1) php artisan make:migration create_whats360_events_table  (columns below)
// 2) Route::post('/whats360/webhook', [Whats360WebhookController::class, 'handle']);
//    and exclude that route from CSRF in bootstrap/app.php (webhooks cannot send CSRF tokens).
// Documented fields: phone, sender_name, message, message_id, chat_jid, timestamp, media_url, instance_id.

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class Whats360WebhookController extends Controller
{
    public function handle(Request $request)
    {
        $d = $request->json()->all();
        if (!is_array($d) || empty($d['message_id'])) {
            return response()->json(['status' => 'ignored'], 200);
        }
        // Schema: whats360_events(message_id PRIMARY KEY, phone, sender_name, message, chat_jid, timestamp, media_url, instance_id)
        $inserted = DB::table('whats360_events')->insertOrIgnore([
            'message_id'  => (string) $d['message_id'],
            'phone'       => (string) ($d['phone'] ?? ''),
            'sender_name' => (string) ($d['sender_name'] ?? ''),
            'message'     => (string) ($d['message'] ?? ''),
            'chat_jid'    => (string) ($d['chat_jid'] ?? ''),
            'timestamp'   => (string) ($d['timestamp'] ?? ''),
            'media_url'   => (string) ($d['media_url'] ?? ''),
            'instance_id' => (string) ($d['instance_id'] ?? ''),
        ]);
        return response()->json(['status' => $inserted ? 'stored' : 'duplicate'], 200);
    }
}
