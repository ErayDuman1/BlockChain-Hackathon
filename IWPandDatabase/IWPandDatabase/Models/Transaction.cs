using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace IWPandDatabase.Models
{
    public class Transaction
    {
        [Display(Name = "Message")]
        public Decimal Message { get; set; }

        [Display(Name = "Sent ")]
        public string Sent { get; set; }

        [Display(Name = "Sender")]
        public string Sender { get; set; }

        [Display(Name = "Private Key")]
        public string PrivateKey { get; set; }

        [Display(Name = "Message Signature")]
        public string MessageSignature { get; set; }

        [Display(Name = "Verify Amount")]
        public decimal verifyAmount { get; set; }

        [Display(Name = "Verify Sent ")]
        public string verifySent { get; set; }

        [Display(Name = "Verify Sender")]
        public string verifySender { get; set; }

        [Display(Name = "Verify Signature")]
        public string verifySignature { get; set; }

        public bool verify = false;
    }
}